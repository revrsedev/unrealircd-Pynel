from django.shortcuts import render, get_object_or_404
from .models import IrcServer
from .utils import perform_rpc_call
from requests.auth import HTTPBasicAuth
from django.conf import settings
import requests

def index(request):
    # RPC call details
    url = settings.RPC_API_URL
    username = settings.RPC_API_USERNAME
    password = settings.RPC_API_PASSWORD
    
    rpc_request = {
        "jsonrpc": "2.0",
        "method": "stats.get",
        "params": {},
        "id": 123
    }
    
    response = requests.post(url, json=rpc_request, auth=HTTPBasicAuth(username, password))
    data = response.json()
    
    if 'result' in data:
        stats = data['result']
    else:
        stats = {}
    
    return render(request, 'ircd/index.html', {'stats': stats})

def server_detail(request, server_id):
    server = get_object_or_404(IrcServer, pk=server_id)
    
    # Perform the RPC call
    response = perform_rpc_call("stats.get", {})
    
    if 'error' in response:
        server_info = {"error": response['error']}
    else:
        server_info = response

    return render(request, 'ircd/server_detail.html', {'server': server, 'info': server_info})


