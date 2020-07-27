import requests
import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse 
from social_django.models import UserSocialAuth

@user_passes_test(lambda u: u.is_anonymous, login_url='/')
def login(request):
	return render(request, 'login.html')

@login_required
def mainpage(request):
	user = request.user
	if user.social_auth.filter(provider='vk-oauth2'):
		social = user.social_auth.get(provider='vk-oauth2')
		token = social.extra_data['access_token']

		url_friends = 'https://api.vk.com/method/friends.get'
		friends_params = {
			'v': '5.52',
			'access_token': token,
			'count': '5',
			'fields': 'city, online, photo_100',
		}
		friends_json = requests.get(url=url_friends, params=friends_params).text
		friends = json.loads(friends_json)['response']['items']

		myself_id = social.extra_data['id']
		url_myself = f'https://api.vk.com/method/users.get?v=5.52&user_ids={myself_id}&fields=photo_200&access_token={token}'
		myself_json = requests.get(url=url_myself).text
		myself = json.loads(myself_json)['response'][0]
		return render(request, 'vk_friends.html', {'friends' : friends, 'myself': myself})
	
	if user.social_auth.filter(provider='facebook'):
		social = user.social_auth.get(provider='facebook')
		ex = social.extra_data
		return render(request, 'fb_develop.html', {'ex': ex})