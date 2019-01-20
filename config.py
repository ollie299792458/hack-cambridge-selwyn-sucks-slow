# Register your third party application on http://developers.monzo.com by logging in with your personal 
# Monzo account. Copy this file into config.py, and enter your credentials into the file.
MONZO_CLIENT_ID = "oauth2client_00009eyICg6cPB2O93Fm6r"
MONZO_CLIENT_SECRET = "mnzconf.lxEV/CbxJtLFjpxwwEN5U8CnN5AzgQni16SVzBNuCj8rtONiVZDZgG637rpH+cfTklu5YojzmgFfmvkk20e1"

# Configurations you should not need to change.
MONZO_OAUTH_HOSTNAME = "auth.monzo.com"
MONZO_API_HOSTNAME = "api.monzo.com"
MONZO_RESPONSE_TYPE = "code"
MONZO_AUTH_GRANT_TYPE = "authorization_code"
MONZO_REFRESH_GRANT_TYPE = "refresh_token"
MONZO_OAUTH_REDIRECT_URI = "http://localhost:8080/oauth2callbackmonzo/" # For receiving the auth code, not currently used.
MONZO_CLIENT_IS_CONFIDENTIAL = True 
# If your application runs on a backend server with client secret hidden from user, it should be registered 
# as confidential and will have the ability to refresh access tokens.
