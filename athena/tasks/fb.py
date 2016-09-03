import argparse

from facebookads.api import FacebookAdsApi
from facebookads import objects
import facebook

if __name__ == "__main__":    
    parser = argparse.ArgumentParser()
    parser.add_argument("--fbApp", help="fb app key", required=True)
    parser.add_argument("--fbSecret", help="fb secret key", required=True)
    args = parser.parse_args()
    
    token = facebook.GraphAPI().get_app_access_token(args.fbApp, args.fbSecret)
    FacebookAdsApi.init(args.fbApp, args.fbSecret, token)

    me = objects.AdUser(fbid='me')
    my_accounts = list(me.get_ad_accounts())

    #my_account = my_accounts[0]
    #my_account.remote_read(fields=[objects.AdAccount.Field.amount_spent])