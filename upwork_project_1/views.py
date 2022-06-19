from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import logout

def index(request):
    if request.user.is_superuser:
      logout(request)

    return redirect('/senior_panel/')

