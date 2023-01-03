from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseNotFound

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
		"january": "Eat no meat!",
		"february": "Learn Django 20 min a day!",
		"march": "Walk at least 5 km every day!",
		"april": "Cycle every day to work!",
		"may": "Read at least 5 pages from a book a day!",
		"june": "Don't use social networks!",
		"july": "Swim every day!",
		"august": "Learn React 20 min a day!",
		"september": "Code at least 1 hour a day!",
		"october": "Learn AWS 20 min a day!",
		"november": "Create some nice project!",
		"december": "Create nice CV and find a job!",
	}
	if month not in challenges.keys():
		return HttpResponseNotFound(f"The month {month} is not supported")
	challenge = challenges[month]
	return HttpResponse(f"This works!<br><h4>This is {month}'s challenge!</h4><br><h2>{challenge}</h2>")
