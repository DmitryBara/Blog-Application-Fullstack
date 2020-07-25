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
	'scope': 'friends, audio, photos',
	'display': 'page',
	'code': None,
}

friends_params = {
	'v':'5.52',
	'access_token': None,
	'count': '5',
	'fields': 'city, online, photo_100',
}

def startpage(request):
	r = requests.get(url=url_auth, params=params)
	return render(request, 'startpage.html', {'r' : r })

def main (request):
	code = request.GET.get('code')
	url = f"{url_token}?client_id={params['client_id']}&client_secret={params['client_secret']}&redirect_uri={params['redirect_uri']}&code={code}"
	token_dict = json.loads(requests.get(url).text)
	access_token = token_dict['access_token']
	user_id = token_dict['user_id']
	expires_in = token_dict['expires_in']
	friends_params['access_token'] = access_token
	friends_json = requests.get(url=url_friends, params=friends_params).text
	friends_list = json.loads(friends_json)['response']['items']
	l = len(friends_list)
	
	i = 0
	person = friends_list[i]
	u_id = person.get('id')
	first_name = person.get('first_name')
	last_name = person.get('last_name')
	city = person.get('city', {}).get('title')
	photo_url = person.get('photo_100')
	online = person.get('online')

	#return render(request, 'base.html', {'r2' : r2})
	return HttpResponse (str(u_id) +' '+ str(first_name) +' '+ str(last_name) +' '+ str(city) +' '+ str(photo_url) +' '+ str(online))