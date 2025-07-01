import requests
from requests.auth import HTTPBasicAuth
from config import FUSION_URL, FUSION_USERNAME, FUSION_PASSWORD

def fusion_get(endpoint, params=None):
    url = f"{FUSION_URL}{endpoint}"
    response = requests.get(url, auth=HTTPBasicAuth(FUSION_USERNAME, FUSION_PASSWORD), params=params)
    return response

def fusion_patch(endpoint, data):
    url = f"{FUSION_URL}{endpoint}"
    response = requests.patch(url, json=data, auth=HTTPBasicAuth(FUSION_USERNAME, FUSION_PASSWORD))
    return response
