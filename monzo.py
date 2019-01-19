# Contract
# Give me a price, date, text, and email links
# I upload these if they match a debit from the monzo account (date close and price match)
# Fails in the event of multiple matches, returns false

# Download transactions around the date of the data
# Match price, if one match succeed, if multiple pick closest date, if still multiple fail
# Upload data - text & link in notes, (email screenshot as receipt?)

# pipenv install requests
import requests
#
import json

ACCOUNT_ID = 'acc_00009RIBEdUZdFewsGVO7d'

ACCESS_TOKEN = open('monzo-access-token','r').read()[:-1]


def within(date, date):
    pass


def match_and_upload_receipt(price, date, text, link):
    #get all transactions
    #http "https://api.monzo.com/transactions" \
    "Authorization: Bearer $access_token" \
    "account_id==$account_id"
    r = requests.get('https://api.monzo.com/transactions?expand[]=merchant&account_id='+ACCOUNT_ID, \
                     headers={'Authorization': 'Bearer '+ACCESS_TOKEN})
    print("Transaction get: "+str(r))

    transactions = json.loads(r.text)["transactions"];

    candidates = []

    for transaction in transactions :
        if (transaction["amount"] == price) :
            print("Candidate transaction:"+json.dumps(transaction, index=1));
            candidates.append(transaction)

    #get all debits within 2 days of date
    print(json.dumps(transactions, indent=4));


# test
match_and_upload_receipt(0,"hi","by","wy")