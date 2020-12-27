import json

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
    }
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
    }
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
    }
}

reputation_mounts_combined_list_of_names = list(set([*mount_dict_alliance] +
                                                    [*mount_dict_horde]+[*mount_dict_neutral]))

reputation_mounts_combined_dict_of_dicts = {
    **mount_dict_alliance, **mount_dict_horde, **mount_dict_neutral}


# Create list of dictionaries where the keys from the old dict are now name values
newlist = []

for k, v in reputation_mounts_combined_dict_of_dicts.items():
    newlist.append({"name": k, **v})

newerlist = []
for i in newlist:
    newerlist.append({"name": i["name"], "rep_faction": i["faction"]})

print(json.dumps(newerlist))
