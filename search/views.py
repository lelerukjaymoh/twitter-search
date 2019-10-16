from django.shortcuts import render
from search.search import Twitter
import json
import pprint

def home(request):
    return render(request, 'home.html', {})

def search_callback(request):
    # print(request.POST)
    twitter = Twitter()
    # access_token = twitter.get_bearer_token()
    access_token = 'AAAAAAAAAAAAAAAAAAAAAA9P%2FwAAAAAAiZ37zaDw3guSW3%2Bn4p4K5xdWqDs%3DcCB1mVjZKlFJ9w3WCUFi3k4OQPF9lKWpiYz0EqXPPLDR9msa5D'
    response = twitter.search(access_token)
    pprint.pprint(response.json())
    
    return render(request, 'search_callback.html', {})