import wowapi
import json

# Get token
token = wowapi.get_token()

if token:
    # Full dict:
    # reputation_mounts = [{"name": "Dusky Waycrest Gryphon", "rep_faction": "Order of Embers"}, {"name": "Smokey Charger", "rep_faction": "Order of Embers"}, {"name": "Proudmoore Sea Scout", "rep_faction": "Proudmoore Admiralty"}, {"name": "Admiralty Stallion", "rep_faction": "Proudmoore Admiralty"}, {"name": "Stormsong Coastwatcher", "rep_faction": "Storm's Wake"}, {"name": "Dapple Gray", "rep_faction": "Storm's Wake"}, {"name": "Dusty Rockhide", "rep_faction": "Council of Exarchs"}, {"name": "Armored Irontusk", "rep_faction": "Sha'tari Defense"}, {"name": "Deathtusk Felboar", "rep_faction": "Vol'jin's Headhunters"}, {"name": "Expedition Bloodswarmer", "rep_faction": "Talanji's Expedition"}, {"name": "Captured Swampstalker", "rep_faction": "Talanji's Expedition"}, {"name": "Alabaster Hyena", "rep_faction": "Voldunai"}, {"name": "Voldunai Dunescraper", "rep_faction": "Voldunai"}, {"name": "Cobalt Pterrordax", "rep_faction": "Zandalari Empire"}, {"name": "Spectral Pterrorwing", "rep_faction": "Zandalari Empire"}, {"name": "Swift Frostwolf", "rep_faction": "Frostwolf Orcs"}, {"name": "Ironside Warwolf", "rep_faction": "Laughing Skull Orcs"}, {
    #    "name": "Wastewander Skyterror", "rep_faction": "Ultum Accord"}, {"name": "Rustbolt Resistor", "rep_faction": "Rustbolt Resistance"}, {"name": "Unshackled Waveray", "rep_faction": "The Unshackled"}, {"name": "Ankoan Waveray", "rep_faction": "Waveblade Ankoan"}, {"name": "Amethyst Ruinstrider", "rep_faction": "Argussian Reach"}, {"name": "Beryl Ruinstrider", "rep_faction": "Argussian Reach"}, {"name": "Cerulean Ruinstrider", "rep_faction": "Argussian Reach"}, {"name": "Russet Ruinstrider", "rep_faction": "Argussian Reach"}, {"name": "Sable Ruinstrider", "rep_faction": "Argussian Reach"}, {"name": "Umber Ruinstrider", "rep_faction": "Argussian Reach"}, {"name": "Brinedeep Bottom-Feeder", "rep_faction": "Conjurer Margoss"}, {"name": "Lightforged Warframe", "rep_faction": "Army of the Light"}, {"name": "Bristling Hellboar", "rep_faction": "The Saberstalkers"}, {"name": "Wild Goretusk", "rep_faction": "The Saberstalkers"}, {"name": "Shadowmane Charger", "rep_faction": "Arakkoa Outcasts"}, {"name": "Corrupted Dreadwing", "rep_faction": "Order of the Awakened"}, {"name": "Domesticated Razorback", "rep_faction": "Steamwheedle Preservation Society"}]
    # Testing dict:
    reputation_mounts = [{"name": "Dusky Waycrest Gryphon", "rep_faction": "Order of Embers"}, {
        "name": "Proudmoore Sea Scout", "rep_faction": "Proudmoore Admiralty"}]

    # Combine existing key value pairs (**i) with id
    reputation_mounts = [
        {**i, "id": mount.get('data', '').get('id', '')}
        for i in reputation_mounts
        for mount in wowapi.search_mount('us', i['name'], token)
        if mount.get('data', '').get('name', '').get('en_US', '') == i['name']
    ]

    # Use id to query mounts and add more information to each mount
    reputation_mounts = [
        {**i, **wowapi.mount_id('us', i.get('id' or 0), token)}
        for i in reputation_mounts
    ]

    # For each item in reputation_mounts, add faction data
    reputation_mounts = [
        # For each faction from the query, keep if it's a rep faction
        # Add id to rep_faction of each mount
        {**mount, 'rep_faction_id': faction.get('id' '')}
        # For each mount in repugation_mounts
        for mount in reputation_mounts
        for faction in wowapi.reputation_faction('us', token)
        if faction.get('name', '') == mount["rep_faction"]
    ]

    # Save to file
    with open('wow-toons/reputation_mounts_rep_id.json', 'w') as json_file:
        json.dump(reputation_mounts, json_file)
