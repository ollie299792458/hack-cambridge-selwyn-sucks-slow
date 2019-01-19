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
#
from datetime import timedelta, datetime

ACCOUNT_ID = 'acc_00009RIBEdUZdFewsGVO7d'

ACCESS_TOKEN = open('monzo-access-token','r').read()[:-1]


#price integer pennies, date is datetime, text is string, link is string
def match_and_upload_receipt(price, datetime, text, link):
    #get all transactions
    #http "https://api.monzo.com/transactions" \
    "Authorization: Bearer $access_token" \
    "account_id==$account_id"

    since = (datetime - timedelta(days=7)).isoformat()+'Z'
    before = (datetime + timedelta(days=7)).isoformat()+'Z'

    r = requests.get('https://api.monzo.com/transactions?expand[]=merchant&account_id='+ACCOUNT_ID+'&since='+since+
                     '&before'+before, headers={'Authorization': 'Bearer '+ACCESS_TOKEN})
    print("Transaction get: "+str(r))

    transactions = json.loads(r.text)["transactions"]

    candidates = []

    for transaction in transactions :
        #print(transaction)
        if transaction["amount"] == price:
            #check if debit transaction
            print("Candidate transaction:"+str(transaction))
            candidates.append(transaction)

    if len(candidates) == 0:
        print("No matching transaction found")
        return

    candidate = candidates[0]

    if len(candidates) > 1 :
        min_candidate = candidate
        #find closest

    candidate['notes'] = text + "\n Link: "+ link;

    print(candidate)

    r = requests.patch('https://api.monzo.com/transactions/'+candidate['id'], headers={'Authorization': 'Bearer '+ACCESS_TOKEN}, data={'transaction':candidate})
    print("Transaction patch: "+str(r))


# test
match_and_upload_receipt(-1010, datetime(2019,1,2),"Testing testing 1 2 3 receipt muncher","downloadmoreram.com")