from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import User
from .forms import PictureForm

def index(request):
    context = {}
    return render(request, 'index.html', context)

def user_panel(request, user_id):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(user_id)
            return HttpResponse('successfully uploaded')
    else:
        form = PictureForm()

    context = { 'user': User.objects.get(pk=user_id), 'form': form }
    return render(request, "user_panel.html", context)
