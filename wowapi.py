# API Module
import os
from dotenv import load_dotenv  # In Ubuntu 20.04, sudo apt install python3-dotenv
import requests
from requests.auth import HTTPBasicAuth
import json


def get_token():
    # Load secrets from .env
    load_dotenv()
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    api_url = 'https://us.battle.net/oauth/token'
    body = {"grant_type": 'client_credentials'}
    auth = HTTPBasicAuth(client_id, client_secret)
    return requests.post(api_url, data=body, auth=auth).json().get(
        'access_token', '') or ''


def search_mount(region, name, access_token):
    url = f'https://{region}.api.blizzard.com/data/wow/search/mount?namespace=static-us&locale=en_US&name.en_US={name}&orderby=id&_page=1'
    return requests.get(url, headers={
        'Authorization': f'Bearer {access_token}'}).json().get('results', '') or ''


def mount_id(region, m_id, access_token):
    url = f'https://{region}.api.blizzard.com/data/wow/mount/{m_id}?namespace=static-us&locale=en_US'
    return requests.get(url, headers={
        'Authorization': f'Bearer {access_token}'}).json()


def reputation_faction(region, access_token):
    url = f'https://{region}.api.blizzard.com/data/wow/reputation-faction/index?namespace=static-us&locale=en_US'
    return requests.get(url, headers={
        'Authorization': f'Bearer {access_token}'}).json().get('factions', []) or []


def collections_mounts(region, realm, character, access_token):
    url = f'https://{u_region}.api.blizzard.com/profile/wow/character/{realm}/{character}/collections/mounts?namespace=profile-us&locale=en_US'
    return requests.get(url, headers={
        'Authorization': f'Bearer {access_token}'}).json().get('mounts', []) or []


# Static variables
u_region = 'us'
api_url_char = f'https://{u_region}.api.blizzard.com/profile/wow/character/'
api_url_data = f'https://{u_region}.api.blizzard.com/data/wow/'
namespace_static = '?namespace=static-us'
namespace_dynamic = '?namespace=dynamic-us'
namespace_profile = '?namespace=profile-us'
locale = '&locale=en_US'
