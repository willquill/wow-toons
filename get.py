import os
from dotenv import load_dotenv  # In Ubuntu 20.04, sudo apt install python3-dotenv
import requests
from requests.auth import HTTPBasicAuth
import json

# Notes
# In the API provided by Blizzard, there is no way to associate a mount with a specific faction, so that must be hardcoded.
# I hardcoded this into faction_mounts.


def get_json(region, client_id, client_secret, url):
    # First get an access token
    api_url = "https://{}.battle.net/oauth/token".format(region)
    body = {"grant_type": 'client_credentials'}
    auth = HTTPBasicAuth(client_id, client_secret)
    token = requests.post(api_url, data=body, auth=auth).json().get(
        'access_token', '')

    # Now use token to query API
    return requests.get(url, headers={
        "Authorization": "Bearer {}".format(token)}).json()


# Load variables from .env
load_dotenv()
app_id = os.getenv('CLIENT_ID')
app_secret = os.getenv('CLIENT_SECRET')

# Dynamic variables from user
u_region = 'us'
u_realm = 'archimonde'
u_character = 'loopn'

# Static variables
token_url = 'https://{}.battle.net/oauth/token'.format(u_region)
api_url_char = 'https://{}.api.blizzard.com/profile/wow/character/'.format(
    u_region)
api_url_data = 'https://{}.api.blizzard.com/data/wow/'.format(u_region)
namespace_static = '?namespace=static-us'
namespace_dynamic = '?namespace=dynamic-us'
namespace_profile = '?namespace=profile-us'
locale = '&locale=en_US'

# Get appearance
a = get_json(u_region, app_id, app_secret, api_url_char +
             '{}/{}/{}{}{}'.format(u_realm, u_character, 'appearance', namespace_profile, locale))

# Get mounts
m = get_json(u_region, app_id, app_secret, api_url_char +
             '{}/{}/{}{}{}'.format(u_realm, u_character, 'collections/mounts', namespace_profile, locale))

# Get reputation
r = get_json(u_region, app_id, app_secret, api_url_char +
             '{}/{}/{}{}{}'.format(u_realm, u_character, 'reputations', namespace_profile, locale))

faction_mounts = [{
    "Faction": "Order of Embers",
    "Side": "Alliance",
    "Mounts": ["Dusky Waycrest Gryphon", "Smokey Charger"]
}, {
    "Faction": "Proudmoore Admiralty",
    "Side": "Alliance",
    "Mounts": ["Proudmoore Sea Crest", "Admiralty Stallion"]
}, {
    "Faction": "Storm's Wake",
    "Side": "Alliance",
    "Mounts": ["Stormsong Coastwatcher", "Dapple Gray"]
}, {
    "Faction": "Talanji's Expedition",
    "Side": "Horde",
    "Mounts": ["Expedition Bloodswarmer", "Captured Swampstalker"]
}, {
    "Faction": "Voldunai",
    "Side": "Horde",
    "Mounts": ["Alabaster Hyena", "Voldunai Dunescraper"]
}, {
    "Faction": "Zandalari Empire",
    "Side": "Horde",
    "Mounts": ["Cobalt Pterrordax", "Spectral Pterrorwing"]
}
    # add the 4 neutral factions
]

# Determine eligibility based on Exalted already
for i in r['reputations']:
    if i['faction']['name'] in bfa_factions_with_mounts:
        if i['standing']['name'] == 'Exalted':
            print('You are eligible for a mount from ' + i['faction']['name'])
            # Add a function to see if you already have the mount

# Get game mounts
gm = get_json(u_region, app_id, app_secret, api_url_data +
              '{}{}{}'.format('mount/index', namespace_static, locale))

# Get game mounts specific
gms = get_json(u_region, app_id, app_secret, api_url_data +
               '{}{}{}'.format('mount/1060', namespace_static, locale))

# Get game factions
gf = get_json(u_region, app_id, app_secret, api_url_data +
              '{}{}{}'.format('reputation-faction/index', namespace_static, locale))

# Get game factions specific
gfs = get_json(u_region, app_id, app_secret, api_url_data +
               '{}{}{}'.format('reputation-faction/2158', namespace_static, locale))

# For testing in case you want to save the json locally
with open('/home/will/repos/wow-toons/{}'.format('whatever.json'), 'w') as json_file:
    json.dump(gms, json_file)
