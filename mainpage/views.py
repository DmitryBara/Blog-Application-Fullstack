from django.shortcuts import render
from django.http import HttpResponse 
#from .models import *
import requests
from django.urls import reverse
import time

friends_request = 'https://api.vk.com/method/friends.getOnline?v=5.52&access_token='
url_auth = 'https://oauth.vk.com/authorize'
url_token = 'https://oauth.vk.com/access_token'

params = {
	'client_id':'7546793',
	'client_secret': 'eYRacdSAyJcBXck5jYfQ',
	'redirect_uri': 'https://dmitrybara-mysite1.herokuapp.com/main',
	'response_type': 'code',
	'scope': 'friends, audio, video',
	'display': 'page',
	'code': '',
}

def startpage(request, code = None):
	r = requests.get(url=url_auth, params=params)
	return render(request, 'startpage.html', {'auth_url_params' : r.url})
	#return HtmlResponse (r1.url)

def main (request):
	code = request.GET.get('code')
	url = f"{url_token}?client_id={params['client_id']}&client_secret={params['client_secret']}&redirect_uri={params['redirect_uri']}&code={code}"
	token = requests.get(url)
	#r2 = requests.get(url = url)
	#return render(request, 'base.html', {'r2' : r2})
	#return HttpResponse (r2.text)
	return HttpResponse (url, str(token))