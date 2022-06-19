from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import User, UserInfo, Picture
from .forms import PictureForm

def index(request):
    context = {}
    return render(request, 'index.html', context)

@login_required
def user_panel(request):
    user = request.user
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(user.id)
            return redirect('/senior_panel/')
    else:
        form = PictureForm()

    user_info = UserInfo.objects.get(pk=user)

    context = { 'user': user, 'user_info': user_info, 'form': form }
    return render(request, "user_panel.html", context)

@login_required
def delete_picture(request, picture_id):
    picture = Picture.objects.get(pk=picture_id)
    picture.delete()
    return redirect('/senior_panel/')

@login_required
def logout_view(request):
    return redirect('/accounts/logout')
