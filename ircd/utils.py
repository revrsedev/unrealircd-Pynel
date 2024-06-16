import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings
import json

def perform_json_rpc_call():
    url = settings.RPC_API_URL
    username = settings.RPC_API_USERNAME
    password = settings.RPC_API_PASSWORD
    rpc_request = {
        "jsonrpc": "2.0",
        "method": "stats.get",
        "params": {},
        "id": 123
    }
    try:
        response = requests.post(url, json=rpc_request, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Request Error:", e)
        return {"error": str(e)}
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)
        return {"error": "Invalid JSON received"}

def perform_rpc_call(method, params):
    url = settings.RPC_API_URL
    username = settings.RPC_API_USERNAME
    password = settings.RPC_API_PASSWORD
    rpc_request = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 123
    }
    try:
        response = requests.post(url, json=rpc_request, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Request Error:", e)
        return {"error": str(e)}
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)
        return {"error": "Invalid JSON received"}
