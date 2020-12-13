import os
from dotenv import load_dotenv  # In Ubuntu 20.04, sudo apt install python3-dotenv
import requests
from requests.auth import HTTPBasicAuth
import json

### Notes ###
# In the API provided by Blizzard, some things are not available, so they had to be hardcoded in this script.
# Hardcoded items:
# - Reputation faction required for a mount
# - Reputation tier required for a mount
# - Gold cost for each mount
# - Currency for each mount

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
u_realm = 'hyjal'
u_character = 'soulebreaker'

# Static variables
token_url = 'https://{}.battle.net/oauth/token'.format(u_region)
api_url_char = 'https://{}.api.blizzard.com/profile/wow/character/'.format(
    u_region)
api_url_data = 'https://{}.api.blizzard.com/data/wow/'.format(u_region)
namespace_static = '?namespace=static-us'
namespace_dynamic = '?namespace=dynamic-us'
namespace_profile = '?namespace=profile-us'
locale = '&locale=en_US'

# Mount dict total
# Note: Can refer to a list of keys only with [*mount_dict]
mount_dict_horde = {
    "Expedition Bloodswarmer": {
        "expansion": "Battle for Azeroth",
        "faction": "Talanji's Expedition",
        "reputation": "Exalted",
        "side": "Horde",
        "cost": 10000
    },
    "Captured Swampstalker": {
        "expansion": "Battle for Azeroth",
        "faction": "Talanji's Expedition",
        "reputation": "Exalted",
        "side": "Horde",
        "cost": 90000
    },
    "Alabaster Hyena": {
        "expansion": "Battle for Azeroth",
        "faction": "Voldunai",
        "reputation": "Exalted",
        "side": "Horde",
        "cost": 10000
    },
    "Voldunai Dunescraper": {
        "expansion": "Battle for Azeroth",
        "faction": "Voldunai",
        "reputation": "Exalted",
        "side": "Horde",
        "cost": 90000
    },
    "Cobalt Pterrordax": {
        "expansion": "Battle for Azeroth",
        "faction": "Zandalari Empire",
        "reputation": "Exalted",
        "side": "Horde",
        "cost": 10000
    },
    "Spectral Pterrorwing": {
        "expansion": "Battle for Azeroth",
        "faction": "Zandalari Empire",
        "reputation": "Exalted",
        "side": "Horde",
        "cost": 90000
    },
    "Deathtusk Felboar": {
        "expansion": "Warlords of Draenor",
        "faction": "Vol'jin's Headhunters",
        "reputation": "Exalted",
        "side": "Horde",
        "cost": 2000
    },
    "Swift Frostwolf": {
        "expansion": "Warlords of Draenor",
        "faction": "Frostwolf Orcs",
        "reputation": "Exalted",
        "side": "Horde",
        "cost": 5000,
        "cost_special": 5000,
        "cost_special_currency": "Apexis Crystal" 
    },
    "Ironside Warwolf": {
        "expansion": "Warlords of Draenor",
        "faction": "Laughing Skull Orcs",
        "reputation": "Exalted",
        "side": "Horde",
        "cost": 0
    },
}

mount_dict_alliance = {
    "Dusky Waycrest Gryphon": {
        "expansion": "Battle for Azeroth",
        "faction": "Order of Embers",
        "reputation": "Exalted",
        "side": "Alliance",
        "cost": 90000
    },
    "Smokey Charger": {
        "expansion": "Battle for Azeroth",
        "faction": "Order of Embers",
        "reputation": "Exalted",
        "side": "Alliance",
        "cost": 10000
    },
    "Proudmoore Sea Scout": {
        "expansion": "Battle for Azeroth",
        "faction": "Proudmoore Admiralty",
        "reputation": "Exalted",
        "side": "Alliance",
        "cost": 90000
    },
    "Admiralty Stallion": {
        "expansion": "Battle for Azeroth",
        "faction": "Proudmoore Admiralty",
        "reputation": "Exalted",
        "side": "Alliance",
        "cost": 10000
    },
    "Stormsong Coastwatcher": {
        "expansion": "Battle for Azeroth",
        "faction": "Storm's Wake",
        "reputation": "Exalted",
        "side": "Alliance",
        "cost": 90000
    },
    "Dapple Gray": {
        "expansion": "Battle for Azeroth",
        "faction": "Storm's Wake",
        "reputation": "Exalted",
        "side": "Alliance",
        "cost": 10000
    },
    "Dusty Rockhide": {
        "expansion": "Warlords of Draenor",
        "faction": "Council of Exarchs",
        "reputation": "Exalted",
        "side": "Alliance",
        "cost": 5000,
        "cost_special": 5000,
        "cost_special_currency": "Apexis Crystal"
    },
    "Armored Irontusk": {
        "expansion": "Warlords of Draenor",
        "faction": "Sha'tari Defense",
        "reputation": "Exalted",
        "side": "Alliance",
        "cost": 5000,
        "cost_special": 5000,
        "cost_special_currency": "Apexis Crystal" 
    },
    "Deathtusk Felboar": {
        "expansion": "Warlords of Draenor",
        "faction": "Hand of the Prophet",
        "reputation": "Exalted",
        "side": "Alliance",
        "cost": 2000
    },
}

mount_dict_neutral = {
    "Wastewander Skyterror": {
        "expansion": "Battle for Azeroth",
        "faction": "Ultum Accord",
        "reputation": "Exalted",
        "side": "Neutral",
        "cost": 24000
    },
    "Rustbolt Resistor": {
        "expansion": "Battle for Azeroth",
        "faction": "Rustbolt Resistance",
        "reputation": "Exalted",
        "side": "Neutral",
        "cost": 524288
    },
    "Unshackled Waveray": {
        "expansion": "Battle for Azeroth",
        "faction": "The Unshackled",
        "reputation": "Exalted",
        "side": "Neutral",
        "cost_special": 250,
        "cost_special_currency": "Prismatic Manapearl"
    },
    "Ankoan Waveray": {
        "expansion": "Battle for Azeroth",
        "faction": "Waveblade Ankoan",
        "reputation": "Exalted",
        "side": "Neutral",
        "cost_special": 250,
        "cost_special_currency": "Prismatic Manapearl"
    },
    "Amethyst Ruinstrider": {
        "expansion": "Legion",
        "faction": "Argussian Reach",
        "reputation": "Exalted",
        "side": "Neutral",
        "cost": 10000
    },
    "Beryl Ruinstrider": {
        "expansion": "Legion",
        "faction": "Argussian Reach",
        "reputation": "Exalted",
        "side": "Neutral",
        "cost": 10000
    },
    "Cerulean Ruinstrider": {
        "expansion": "Legion",
        "faction": "Argussian Reach",
        "reputation": "Exalted",
        "side": "Neutral",
        "cost": 10000
    },
    "Russet Ruinstrider": {
        "expansion": "Legion",
        "faction": "Argussian Reach",
        "reputation": "Exalted",
        "side": "Neutral",
        "cost": 10000
    },
    "Sable Ruinstrider": {
        "expansion": "Legion",
        "faction": "Argussian Reach",
        "reputation": "Exalted",
        "side": "Neutral",
        "cost": 10000
    },
    "Umber Ruinstrider": {
        "expansion": "Legion",
        "faction": "Argussian Reach",
        "reputation": "Exalted",
        "side": "Neutral",
        "cost": 10000
    },
    "Brinedeep Bottom-Feeder": {
        "expansion": "Legion",
        "faction": "Conjurer Margoss",
        "reputation": "Best Friend",
        "side": "Neutral",
        "cost_special": 100,
        "cost_special_currency": "Drowned Mana"
    },
    "Lightforged Warframe": {
        "expansion": "Legion",
        "faction": "Army of the Light",
        "reputation": "Exalted",
        "side": "Neutral",
        "cost": 500000
    },
    "Bristling Hellboar": {
        "expansion": "Warlords of Draenor",
        "faction": "The Saberstalkers",
        "reputation": "Exalted",
        "side": "Neutral",
        "cost_special": 5000,
        "cost_special_currency": "Blackfang Claw"
    },
    "Wild Goretusk": {
        "expansion": "Warlords of Draenor",
        "faction": "The Saberstalkers",
        "reputation": "Honored",
        "side": "Neutral",
        "cost_special": 1000,
        "cost_special_currency": "Blackfang Claw"
    },
    "Shadowmane Charger": {
        "expansion": "Warlords of Draenor",
        "faction": "Arakkoa Outcasts",
        "reputation": "Exalted",
        "side": "Neutral",
        "cost": 5000,
        "cost_special": 5000,
        "cost_special_currency": "Apexis Crystal"
    },
    "Corrupted Dreadwing": {
        "expansion": "Warlords of Draenor",
        "faction": "Order of the Awakened",
        "reputation": "Friendly",
        "side": "Neutral",
        "cost_special": 150000,
        "cost_special_currency": "Apexis Crystal" 
    },
    "Domesticated Razorback": {
        "expansion": "Warlords of Draenor",
        "faction": "Steamwheedle Preservation Society",
        "reputation": "Exalted",
        "side": "Neutral",
        "cost": 5000,
        "cost_special": 5000,
        "cost_special_currency": "Apexis Crystal"
    },
}

#######################################
###### Get Character Information ######
#######################################

# Get appearance
# appearance = get_json(u_region, app_id, app_secret, api_url_char +
#              '{}/{}/{}{}{}'.format(u_realm, u_character, 'appearance', namespace_profile, locale))

# Get list of mounts user has
mount_has = get_json(u_region, app_id, app_secret, api_url_char +
             '{}/{}/{}{}{}'.format(u_realm, u_character, 'collections/mounts', namespace_profile, locale)).get('mounts', []) or []

# Find out which side the character is on
side = get_json(u_region, app_id, app_secret, api_url_char +
             '{}/{}{}{}'.format(u_realm, u_character, namespace_profile, locale)).get("faction", "").get("name", "") or ""

# Get reputation
rep_list = get_json(u_region, app_id, app_secret, api_url_char +
             '{}/{}/{}{}{}'.format(u_realm, u_character, 'reputations', namespace_profile, locale)).get("reputations", []) or []

# Sample item in mount_has:
# {
#     "mount": {
#         "key": {
#             "href": "https://us.api.blizzard.com/data/wow/mount/6?namespace=static-9.0.2_36532-us"
#     },
#         "name": "Brown Horse",
#         "id": 6
#     },
#     "is_useable": false
#}

# Created flattened list of mounts
mount_has = [i.get("mount", "").get("name", "") for i in mount_has] or []

# Create combined dictionary
mount_dict = {}
if side == "Horde":
    mount_dict = {**mount_dict_horde, **mount_dict_neutral}
elif side == "Alliance":
    mount_dict = {**mount_dict_alliance, **mount_dict_neutral}

mount_missing = [i for i in [*mount_dict] if i not in mount_has] or []

# Sample item in rep_list:
# {
#     "faction": {
#         "key": {
#             "href": "https://us.api.blizzard.com/data/wow/reputation-faction/76?namespace=static-9.0.2_36532-us"
#         },
#         "name": "Orgrimmar",
#         "id": 76
#     },
#     "standing": {
#         "raw": 6690,
#         "value": 3690,
#         "max": 6000,
#         "tier": 4,
#         "name": "Friendly"
#     }
# }

# Dictionary showing the raw value needed to reach the tier
rep_dict = {
    "Neutral": 0,
    "Friendly": 6000,
    "Honored": 12000,
    "Revered": 21000,
    "Exalted": 42000,
    "Stranger": 0,
    "Acquaintance": 8400,
    "Buddy": 16800,
    "Friend": 25200,
    "Good Friend": 33600,
    "Best Friend": 42000
}

# For each mount in missing list, create a dictionary of the mount, mount faction, and percentage toward tier

# NEED TO MODIFY THIS TO ACCOUNT FOR SPECIAL CURRENCIES

mount_missing_details = {}
for mount in mount_missing:
    for r in rep_list:
        if mount_dict[mount].get("faction", "") or "" == r.get("faction", "").get("name", "") or "":
            mount_missing_details[mount] = {
                "faction": mount_dict.get(mount, "").get("faction", "") or "",
                "current_tier": r.get("standing", "").get("name", "") or "",
                "required_tier": mount_dict.get(mount, "").get("reputation", "") or "",
                # standing/raw divided by required tier's value in rep_dict
                "percent_complete": round(r.get("standing", 0).get("raw", 0)/rep_dict.get(mount_dict.get(mount, "").get("reputation", "") or ""), 2) or 0,
                "required_gold": mount_dict.get(mount, "").get("cost", "") or 0
            }

# Determine gold cost for eligible mount purchases
total_gold = 0
for k, v in mount_missing_details.items():
    if v.get('percent_complete', '') or '' >= 1.0:
        total_gold = total_gold + v.get('required_gold', '') or ''

print("You have already met the reputation requirements to get some mounts you don't have.\n")
print("To get all eligible mounts right now would cost you " + str('{:,}').format(total_gold) + " gold.")



############################################
###### Troubleshooting and future use ######
############################################

# Get game mounts
# gm = get_json(u_region, app_id, app_secret, api_url_data +
#               '{}{}{}'.format('mount/index', namespace_static, locale))

# # Get game mounts specific
# gms = get_json(u_region, app_id, app_secret, api_url_data +
#                '{}{}{}'.format('mount/1060', namespace_static, locale))

# # Get game factions
# gf = get_json(u_region, app_id, app_secret, api_url_data +
#               '{}{}{}'.format('reputation-faction/index', namespace_static, locale))

# # Get game factions specific
# gfs = get_json(u_region, app_id, app_secret, api_url_data +
#                '{}{}{}'.format('reputation-faction/2158', namespace_static, locale))

# # For testing in case you want to save the json locally
# with open('/home/will/repos/wow-toons/{}'.format('mounts.json'), 'w') as json_file:
#     json.dump(m, json_file)


# # For testing in case you want to save the json locally
#with open('/home/will/repos/wow-toons/{}'.format('reputation.json'), 'w') as json_file:
#     json.dump(r, json_file)
