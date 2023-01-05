from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
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


def index(request):
    months = list(monthly_challenges.keys())
    index_response = "<ul>"
    for month in months:
        parent_url = reverse(f"month_challenge_str", args = [month])
        month_response = f"<li><a href = {parent_url}>{month.capitalize()}</a></li>"
        index_response += month_response
    index_response += "</ul>"

    return HttpResponse("<h2>This works! This is challenges' index!</h2>" + index_response)


def monthly_challenge_by_num(request, month):
    months = list(monthly_challenges.keys())
    try:
        redirect_month = months[month - 1]
        redirect_url = reverse(f"month_challenge_str", args=[redirect_month])
        return HttpResponseRedirect(redirect_url)
    except:
        return HttpResponseNotFound(f"The month number {month} is not valid!")


def monthly_challenge_by_str(request, month):
    try:
        challenge = monthly_challenges[month]
        return HttpResponse(f"This works!<br><h4>This is {month}'s challenge!</h4><br><h2>{challenge}</h2>")
    except:
        return HttpResponseNotFound(f"The month {month} is not supported")
