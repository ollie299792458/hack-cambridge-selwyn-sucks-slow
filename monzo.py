# Contract
# Give me a price, date, text, and email links
# I upload these if they match a debit from the monzo account (date close and price match)

# Download transactions around the date of the data
# Match price, if one match succeed, if multiple pick closest date, if still multiple fail
# Upload data - text & link in notes, (email screenshot as receipt?)

# pipenv install requests
import

def match_and_upload_receipt(price, date, text, link):
    #http "https://api.monzo.com/transactions" \
    "Authorization: Bearer $access_token" \
    "account_id==$account_id"




# test