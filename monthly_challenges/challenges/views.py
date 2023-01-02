from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def index(request):
	print(request)
	return HttpResponse("This works!\nThis is challenges' index!")


def january(request):
	print(request)
	return HttpResponse("This works! This is january's challenge!\nEat no meat!")


def february(request):
	print(request)
	return HttpResponse("This works! This is february's challenge!\nLearn Django every day!")


def monthly_challenge(request, month):
	challenges = {
		"january": "This works! This is january's challenge!\nEat no meat!",
		"february": "This works! This is february's challenge!\nLearn Django every day!",
	}
	return HttpResponse(challenges[month])
