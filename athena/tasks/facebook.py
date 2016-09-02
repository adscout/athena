import argparse

from facebookads.api import FacebookAdsApi
from facebookads import objects
import facebook

if __name__ == "__main__":    
    parser = argparse.ArgumentParser()
    parser.add_argument("--fbApp", help="fb app key", required=True)
    parser.add_argument("--fbSecret", help="fb secret key", required=True)
    args = parser.parse_args()
    
    token = facebook.GraphAPI().get_app_access_token(args.fbAPP, args.fbSecret)