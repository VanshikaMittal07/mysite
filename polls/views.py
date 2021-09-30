from datetime import datetime
from datetime import timedelta

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.utils import timezone

from .models import Questions, UrlTokens

# Create your views here.
def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def get_details(request, question_id):
    return HttpResponse('Get details for question id %s' % question_id)

def shorten_path(request, url):
    unique_string = get_random_string(length=16)
    token = UrlTokens(url=url, token=unique_string)

    token.save()
    return HttpResponse('Refer to the link: %s' % unique_string)

def redirect_url(request, token):
    page = UrlTokens.objects.get(token=token)
    if(page.created_at < timezone.now() - timedelta(minutes=1)):
        return HttpResponse('Token has expired. Please regenrate the token')
    return redirect(page.url)
 