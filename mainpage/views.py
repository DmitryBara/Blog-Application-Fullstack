import requests
import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 
from social_django.models import UserSocialAuth # Nonce, Association, Code, DjangoStorage, AbstractUserSocialAuth


def login(request):
	return render(request, 'login.html')

@login_required
def mainpage(request):
	user = request.user
	a = UserSocialAuth.objects.get(user_id=user.id)
	if user.social_auth.filter(provider='vk-oauth2'):
		social = user.social_auth.get(provider='vk-oauth2')
		token = social.extra_data['access_token']
		url_friends = 'https://api.vk.com/method/friends.get'
		friends_params = {
			'access_token': token,
			'count': '5',
			'fields': 'city, online, photo_100',
		}
		friends_json = requests.get(url=url_friends, params=friends_params).text
		#friends = json.loads(friends_json)['response']['items']
	
		#friends = [{'id': 43817, 'first_name': 'Максим', 'last_name': 'Холодняк', 'city': {'id': 2, 'title': 'Санкт-Петербург'}, 'photo_100': 'https://sun6-13.userapi.com/c857416/v857416879/107ff9/ML37gefRTU8.jpg?ava=1', 'online': 1, 'track_code': '58f83b87Zas9qtT7GIMDsURf56woO4bIt52AwOiYeSoMncHPreEIwDfJ5q4djQLlQrdHAcFb5q7F'}, {'id': 57500, 'first_name': 'Таня', 'last_name': 'Узор', 'deactivated': 'deleted', 'online': 0, 'photo_100': 'https://vk.com/images/deactivated_100.png', 'track_code': '1f25b1e50MqEG0sWzne0xWu-iZMuon_7T9qNnx1Yi5bQ4GYVr4a9odx-dhCbcrCRbFYpPsfCH509'}, {'id': 138959, 'first_name': 'Федор', 'last_name': 'Водкин', 'city': {'id': 2, 'title': 'Санкт-Петербург'}, 'photo_100': 'https://sun6-16.userapi.com/impg/c858220/v858220362/11e287/ihmbO6aFUnk.jpg?size=100x0&quality=90&crop=0,81,1620,1620&sign=0f51513b263b7f7eaa95a28b26c4b8ad&c_uniq_tag=re7_OqgZocpdL_-buhNqx715aT8_NVTinKAwcFOuh_4&ava=1', 'online': 0, 'track_code': '34705cecoNGsXz2grQf4XHyFdynDdJCjr4GV0dRM-AdOdwssVx7NuvE6WaemXKNeRwbblzMa57fd6A'}, {'id': 272438, 'first_name': 'Евгений', 'last_name': 'Истомин', 'photo_100': 'https://sun6-19.userapi.com/PEJZEVfk2HQOEe9dBTJ__IxO20VyPf5vcsp_yA/OXON_5mYzco.jpg?ava=1', 'online': 0, 'track_code': 'e35ee60f2qK2W7TzToL683MIsALkdKbeAGm14dNUg1qw5QU4Ur23yeht1PdNhPeiSIscvBQa0cpyAA'}, {'id': 288503, 'first_name': 'Михаил', 'last_name': 'Мишунькин', 'city': {'id': 2, 'title': 'Санкт-Петербург'}, 'photo_100': 'https://sun9-48.userapi.com/c623900/v623900067/10850/z_oOpM1tJo8.jpg?ava=1', 'online': 0, 'track_code': '4dc652de6BLhNuGcsgw73EX6dd0Z9gBlU-fY4tocLe-is9CAU8iFebMF0crrUDfecnnZY-mYd3Ehjg'}] 
		#return render(request, 'mainpage.html', {'friends' : friends})
		return (friends_json)
	
	if user.social_auth.filter(provider='facebook'):
		return HttpResponse ('Facebook')







# url_auth = 'https://oauth.vk.com/authorize'
# url_token = 'https://oauth.vk.com/access_token'
# url_friends = 'https://api.vk.com/method/friends.get?v=5.52&access_token='

# params = {
# 	'client_id':'7546793',
# 	'client_secret': 'eYRacdSAyJcBXck5jYfQ',
# 	'redirect_uri': 'https://dmitrybara-mysite1.herokuapp.com/',
# 	'response_type': 'code',
# 	'scope': 'friends, audio, photos',
# 	'display': 'page',
# 	'code': None,
# }




# def startpage(request):
# 	r = requests.head(url=url_auth, params=params)
# 	return render(request, 'startpage.html', {'r' : r })

# def main (request):
# 	code = request.GET.get('code')
# 	url = f"{url_token}?client_id={params['client_id']}&client_secret={params['client_secret']}&redirect_uri={params['redirect_uri']}&code={code}"
# 	token_dict = json.loads(requests.get(url).text)
# 	access_token = token_dict['access_token']
# 	user_id = token_dict['user_id']
# 	expires_in = token_dict['expires_in']
# 	friends_params['access_token'] = access_token
# 	friends_json = requests.get(url=url_friends, params=friends_params).text
# 	friends_list = json.loads(friends_json)['response']['items']
# 	l = len(friends_list)
	
# 	i = 0
# 	person = friends_list[i]
# 	u_id = person.get('id')
# 	first_name = person.get('first_name')
# 	last_name = person.get('last_name')
# 	city = person.get('city', {}).get('title')
# 	photo_url = person.get('photo_100')
# 	online = person.get('online')

# 	#return render(request, 'base.html', {'r2' : r2})
# 	return HttpResponse (str(u_id) +' '+ str(first_name) +' '+ str(last_name) +' '+ str(city) +' '+ str(photo_url) +' '+ str(online))