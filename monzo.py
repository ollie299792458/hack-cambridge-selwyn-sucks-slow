# Contract
# Give me a price, date, text, and email links
# I upload these if they match a debit from the monzo account (date close and price match)
# Fails in the event of multiple matches, returns false

# Download transactions around the date of the data
# Match price, if one match succeed, if multiple pick closest date, if still multiple fail
# Upload data - text & link in notes, (email screenshot as receipt?)

# pipenv install requests
import uuid

import requests
#
import json
#
from datetime import timedelta, datetime
from main import ReceiptsClient

import main
import receipt_types


#price integer pennies, date is datetime, text is string, link is string
def match_and_upload_receipt(price, date, text, link, ACCOUNT_ID, ACCESS_TOKEN):
    #get all transactions
    #http "https://api.monzo.com/transactions" \
    "Authorization: Bearer $access_token" \
    "account_id==$account_id"

    since = (date - timedelta(days=7)).isoformat()[:-6]+'Z'
    before = (date + timedelta(days=7)).isoformat()[:-6]+'Z'
    r = requests.get('https://api.monzo.com/transactions?expand[]=merchant&account_id='+ACCOUNT_ID+'&since='+since+
                     '&before'+before, headers={'Authorization': 'Bearer '+ACCESS_TOKEN})
    transactions = json.loads(r.text)["transactions"]

    candidates = []

    for transaction in transactions :
        #print(transaction)
        if -transaction["amount"] == abs(price):
            #check if debit transaction
            candidates.append(transaction)

    if len(candidates) == 0:
        return

    candidate = min(candidates, key=lambda x: (datetime.fromisoformat(x['created']) - date).total_seconds())

    # Using a random receipt ID we generate as external ID
    receipt_id = uuid.uuid4().hex

    example_items = [receipt_types.Item(text+" "+link, 1, "", abs(candidate["amount"]), "GBP", 0, [])]

    example_receipt = receipt_types.Receipt("", receipt_id, candidate["id"],
                                            abs(candidate["amount"]), "GBP", "", "", example_items)
    example_receipt_marshaled = example_receipt.marshal()
    print(date.isoformat() + " " + str(example_receipt_marshaled))
    client = requests.put("https://api.monzo.com/transaction-receipts/", data=example_receipt_marshaled, headers={'Authorization': 'Bearer '+ACCESS_TOKEN})

# test
#match_and_upload_receipt(-1010, datetime(2019,1,2),"Testing testing 1 2 3 receipt muncher","downloadmoreram.com")