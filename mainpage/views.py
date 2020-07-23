from django.shortcuts import render
from django.http import HttpResponse 
#from .models import *
import requests
from django.urls import reverse
import time

friends_request = 'https://api.vk.com/method/friends.getOnline?v=5.52&access_token='
auth_url = 'https://oauth.vk.com/authorize'
token_url = 'https://oauth.vk.com/access_token'

params = {
	'client_id':'7546793',
	'client_secret': 'eYRacdSAyJcBXck5jYfQ',
	'redirect_uri': 'localhost:8000/friends',
	'response_type': 'code',
	'scope': 'friends, audio, video',
	'display': 'page',
	'code': '',
}

def login(request, code = None):
	r1 = requests.get(url=auth_url, params=params)
	return render(request, 'login.html', {'r1' : r1})
	#return HtmlResponse (r1.url)

def friends (request):
	code = request.GET.get('code')
	url = f"{token_url}?client_id={params['client_id']}&client_secret={params['client_secret']}&redirect_uri={params['redirect_uri']}&code={code}"
	r2 = requests.get(url = url)
	#return render(request, 'base.html', {'r2' : r2})
	return HttpResponse (r2.text)