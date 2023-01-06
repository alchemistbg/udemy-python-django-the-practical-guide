from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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


def get_months():
    return list(monthly_challenges.keys())


def index(request):
    months = get_months()
    list_items = ""
    for month in months:
        parent_url = reverse(f"month_challenge_str", args=[month])
        list_items += f"<li><a href = {parent_url}>{month.capitalize()}</a></li>"
    index_response = f"<ul>{list_items}</ul>"
    return HttpResponse("<h2>This works! This is challenges' index!</h2>" + index_response)


def monthly_challenge_by_num(request, month):
    months = get_months()
    try:
        redirect_month = months[month - 1]
        redirect_url = reverse(f"month_challenge_str", args=[redirect_month])
        return HttpResponseRedirect(redirect_url)
    except:
        return HttpResponseNotFound(f"The month number {month} is not valid!")


def monthly_challenge_by_str(request, month):
    try:
        challenge = monthly_challenges[month]
        response_data = render_to_string("challenges/challenges.html")
        # return HttpResponse(f"This works!<br><h4>This is {month}'s challenge!</h4><br><h2>{challenge}</h2>")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound(f"The month {month} is not supported")
