from django.shortcuts import render
from django.http import JsonResponse
from .models import *


# Create your views here.

def index(request) :

	members = Member.objects.all()

	context = {'members' : members}

	return render(request, './a.html', context)


def index2(request) :

	return render(request, './b.html')

def index3(request):
	return render(request, './ddd.html')

def check_id(request):

	if request.method == 'GET' :

		print(request.GET.get('user_id',None))
		user_id = request.GET.get('user_id',None)

		"""
		memeber_list = Member.objects.filter(user_id= user_id)
		if member_list:
			result = { "result" : 'true'}
		else :
			result = {"result" : 'false'}
		"""

		try:
			member_list = Member.objects.get(user_id = user_id)
			'''memeber.objects.all()'''
			result = {"result" : 'true'}
		except :
			result = {"result" : 'false'}

	return JsonResponse(result)


def register_member_db(request):

	if request.method == 'POST':

		user_id = request.POST['user_id']
		user_psw = request.POST['user_psw']

		new_member = Member(user_id = user_id, user_psw = user_psw)
		#멤버 객체 생성 
		new_member.save()

		return render(request, './test2.html')