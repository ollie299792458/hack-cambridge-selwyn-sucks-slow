# Contract
# Give me a price, date, text, and email links
# I upload these if they match a debit from the monzo account (date close and price match)

# Download transactions around the date of the data
# Match price, if one match succeed, if multiple pick closest date, if still multiple fail
# Upload data - text & link in notes, (email screenshot as receipt?)

# pipenv install requests
import requests

ACCOUNT_ID = 'acc_00009RIBEdUZdFewsGVO7d'

ACCESS_TOKEN = open('monzo-access-token','r').read()[:-1]

def match_and_upload_receipt(price, date, text, link):
    #http "https://api.monzo.com/transactions" \
    "Authorization: Bearer $access_token" \
    "account_id==$account_id"
    r = requests.get('https://api.monzo.com/transactions?expand[]=merchant&account_id='+ACCOUNT_ID, \
                     headers={'Authorization': 'Bearer '+ACCESS_TOKEN})
    print(r)




# test
match_and_upload_receipt(0,"hi","by","wy")