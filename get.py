import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import json

def create_access_token(client_id, client_secret, region):
    url = "https://{}.battle.net/oauth/token".format(region)
    body = {"grant_type": 'client_credentials'}
    auth = HTTPBasicAuth(client_id, client_secret)

    response = requests.post(url, data=body, auth=auth)
    return response.json()

def get_profile_token(path, filename):
    access_token = create_access_token(client_id, client_secret, u_region).get('access_token', '')
    with open('/home/will/repos/wow-toons/{}'.format(filename), 'w') as json_file:
        path = '/profile/{}'.format(path)
        full_url = api_url+path+namespace_profile+locale
        json.dump(requests.get(full_url, headers={"Authorization": "Bearer {}".format(access_token)}).json(), json_file)

# Load variables from .env
load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

# Dynamic variables from user
u_region = 'us'
u_realm = 'dalaran'
u_character = 'bezwulf'

# Static variables
token_url = 'https://{}.battle.net/oauth/token'.format(u_region)
api_url = 'https://{}.api.blizzard.com'.format(u_region)
redirect_uri = 'https://your.callback/uri'
namespace_static = '?namespace=static-us'
namespace_dynamic = '?namespace=dynamic-us'
namespace_profile = '?namespace=profile-us'
locale = '&locale=en_US'

# Get achievement statistics
get_profile_token('wow/character/{}/{}/achievements/statistics'.format(u_realm, u_character), 'stats.json')

# Get appearance
get_profile_token('wow/character/{}/{}/appearance'.format(u_realm, u_character), 'appearance.json')

# Get mounts
#get_profile_code('user/wow/collections/mounts', 'mounts.json')
