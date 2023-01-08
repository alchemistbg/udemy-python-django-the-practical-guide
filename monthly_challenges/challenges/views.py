from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
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
    "december": None
}


def get_months():
    return list(monthly_challenges.keys())


def index(request):
    months = get_months()
    return render(request, 'challenges/index.html', {
        "months": months
    })


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
        return render(request, 'challenges/challenge.html', {
            "month": month,
            "challenge": challenge
        })
    except:
        raise Http404()
