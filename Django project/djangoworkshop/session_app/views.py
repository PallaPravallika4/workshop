from django.shortcuts import render
from django.http import HttpResponse

def set_session(request):
    request.session['username'] = 'pravallika'
    return HttpResponse("Session data set!")

def get_session(request):
    username = request.session.get('username', 'Guest')
    return HttpResponse(f"Hello, username !")
