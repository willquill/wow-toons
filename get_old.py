import os
from dotenv import load_dotenv  # In Ubuntu 20.04, sudo apt install python3-dotenv
import requests
from requests.auth import HTTPBasicAuth
import json


# - Reputation faction required for a mount
# - Reputation tier required for a mount
# - Gold cost for each mount
# - Currency for each mount


# Created flattened list of mounts
mount_has_namesonly = [i.get("mount", "").get("name", "")
                       for i in mount_has] or []

# Create combined dictionary
mount_dict = {}
if side == "Horde":
    mount_dict = {**mount_dict_horde, **mount_dict_neutral}
elif side == "Alliance":
    mount_dict = {**mount_dict_alliance, **mount_dict_neutral}

mount_missing = [i for i in [*mount_dict]
                 if i not in mount_has_namesonly] or []

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
print("To get all eligible mounts right now would cost you " +
      str('{:,}').format(total_gold) + " gold.")


## TESTING ##
# Get all possible mounts
# mount_index = get_json(u_region, app_id, app_secret, api_url_data +
#                        '{}{}{}'.format('mount/index', namespace_static, locale)).get('mounts', []) or []
# with open('/home/will/repos/wow-toons/{}'.format('mount_index.json'), 'w') as json_file:
#     json.dump(mount_index, json_file)

# Open list of all mounts
# with open('/home/will/repos/wow-toons/mount_index.json') as json_file:
#     mount_index = json.load(json_file)

# reformat missing mounts
# newmount_has = []
# for mount in mount_has:
#     newmount_has.append(mount.get('mount', ''))

# # add mount to index for each mount in mount_index, if mount not in mount_has
# mount_missing = [i for i in mount_index if i not in newmount_has]

# save mount_missing to file
# with open('/home/will/repos/wow-toons/{}'.format('mount_missing.json'), 'w') as json_file:
#     json.dump(mount_missing, json_file)

# For each mount in mount_missing, get more details about it
# thismount = {}
# for mount in mount_index:
#     thismount = get_json(u_region, app_id, app_secret, api_url_data +
#                          '{}/{}{}{}'.format('mount', mount["id"], namespace_static, locale))

#     # For each key:value pair in the dictionary, if the key is not in the mount, add it
#     for k, v in thismount.items():
#         if k not in mount.items():
#             mount[k] = v

############################################
###### Troubleshooting and future use ######
############################################

# Get game mounts
# mount_has = get_json(u_region, app_id, app_secret, api_url_data +
#               '{}{}{}'.format('mount/index', namespace_static, locale))
# print (mount_index)

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
# with open('/home/will/repos/wow-toons/{}'.format('reputation.json'), 'w') as json_file:
#     json.dump(r, json_file)
