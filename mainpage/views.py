import requests
import json

from django.shortcuts import render
from django.http import HttpResponse 
#from .models import *
from django.urls import reverse



url_auth = 'https://oauth.vk.com/authorize'
url_token = 'https://oauth.vk.com/access_token'
url_friends = 'https://api.vk.com/method/friends.get?v=5.52&access_token='

params = {
	'client_id':'7546793',
	'client_secret': 'eYRacdSAyJcBXck5jYfQ',
	'redirect_uri': 'https://dmitrybara-mysite1.herokuapp.com/main',
	'response_type': 'code',
	'scope': 'friends, audio, video',
	'display': 'page',
	'code': None,
}

friends_params = {
	'v':'5.52',
	'access_token': None,
	'order': 'hints',
	'count': '5',
	'fields': 'city, online, photo_100',
}

def startpage(request):
	r = requests.get(url=url_auth, params=params)
	return render(request, 'startpage.html', {'auth_url_params' : r.url})

def main (request):
	code = request.GET.get('code')
	url = f"{url_token}?client_id={params['client_id']}&client_secret={params['client_secret']}&redirect_uri={params['redirect_uri']}&code={code}"
	token_dict = str(requests.get(url).text)
	#token_dict = json.loads(requests.get(url).text)
	#access_token = token_dict['access_token']
	#friends_params['access_token'] = access_token
	#user_id = token_dict['user_id']
	#friends = requests.get(url=url_friends, params=friends_params)


	#return render(request, 'base.html', {'r2' : r2})
	#return HttpResponse (r2.text)
	#return HttpResponse (str(friends.url))
	return HttpResponse (token_dict)