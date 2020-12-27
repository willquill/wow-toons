import wowapi
import json

# Get token
token = wowapi.get_token()

# Dynamic variables from user
u_region = 'us'
u_realm = 'hyjal'
u_character = 'soulebreaker'

#######################################
###### Get Character Information ######
#######################################

if token:

    # Get list of mounts in character's collection
    collections_mounts = [
        i
        for i in wowapi.collections_mounts(u_region, u_realm, u_character, token)
    ]
    print(json.dumps(collections_mounts))


# Get appearance
# appearance = get_json(u_region, app_id, app_secret, api_url_char +
#              '{}/{}/{}{}{}'.format(u_realm, u_character, 'appearance', namespace_profile, locale))


# # Find out which side the character is on
# side = get_json(u_region, app_id, app_secret, api_url_char +
#                 '{}/{}{}{}'.format(u_realm, u_character, namespace_profile, locale)).get("faction", "").get("name", "") or ""

# # Get reputation
# rep_list = get_json(u_region, app_id, app_secret, api_url_char +
#                     '{}/{}/{}{}{}'.format(u_realm, u_character, 'reputations', namespace_profile, locale)).get("reputations", []) or []

# # Sample item in mount_has:
# # {
# #     "mount": {
# #         "key": {
# #             "href": "https://us.api.blizzard.com/data/wow/mount/6?namespace=static-9.0.2_36532-us"
# #     },
# #         "name": "Brown Horse",
# #         "id": 6
# #     },
# #     "is_useable": false
# # }

# mounts_dict = open reputation_mounts.json

# for mount in mount_dict if mount in mount_has:
#     pop from mount_dict(because we want mount_dict to be mounts we care about)


# if token:

#     reputation_mounts = [
#         # Combine existing key value pairs (**i) with id
#         {**i, "id": mount.get('data', '').get('id', '')}
#         for i in reputation_mounts
#         for mount in wowapi.search_mount('us', i['name'], token)
#         if mount.get('data', '').get('name', '').get('en_US', '') == i['name']
#     ]

#     # Use id to query mounts and add more information to each mount
#     reputation_mounts = [
#         {**i, **wowapi.mount_id('us', i.get('id' or 0), token)}
#         for i in reputation_mounts
#     ]

#     print(reputation_mounts)
