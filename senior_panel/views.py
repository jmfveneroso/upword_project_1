from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import User, UserInfo, Picture, CalendarEntry, HeaderEntry
from .forms import PictureForm, CalendarEntryForm, UserInfoForm, HeaderEntryForm

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
            return redirect('/senior_panel/admin')

    form = PictureForm()
    calendar_entry_form = CalendarEntryForm()
    user_info_form = UserInfoForm()

    user_info = UserInfo.objects.get(pk=user)

    context = { 
      'user': user, 
      'user_info': user_info, 
      'calendar_entries': user.get_sorted_calendar_entries(),
      'status_types': user.get_status_types(),
      'status_types_str': ','.join(user.get_status_types()),
      'form': form, 
      'calendar_entry_form': calendar_entry_form,
      'user_info_form': user_info_form,
    }
    return render(request, "user_panel.html", context)

@login_required
def admin_panel(request):
    user = request.user
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(user.id)
            return redirect('/senior_panel/admin')

    form = PictureForm()
    calendar_entry_form = CalendarEntryForm()
    user_info_form = UserInfoForm()

    user_info = UserInfo.objects.get(pk=user)

    context = { 
      'user': user, 
      'user_info': user_info, 
      'calendar_entries': user.get_sorted_calendar_entries(),
      'status_types': user.get_status_types(),
      'status_types_str': ','.join(user.get_status_types()),
      'form': form, 
      'calendar_entry_form': calendar_entry_form,
      'user_info_form': user_info_form,
    }
    return render(request, "admin_panel.html", context)

@login_required
def delete_picture(request, picture_id):
    picture = Picture.objects.get(pk=picture_id)
    picture.delete()
    return redirect('/senior_panel/admin')

@login_required
def add_calendar_entry(request):
    if request.method == 'POST':
        form = CalendarEntryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(request.user.id)

    return redirect('/senior_panel/admin')

@login_required
def add_header_entry(request):
    print('Entrei uhul')
    if request.method == 'POST':
        form = HeaderEntryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(request.user.id)

    return redirect('/senior_panel/admin')

@login_required
def delete_calendar_entry(request, entry_id):
    entry = CalendarEntry.objects.get(pk=entry_id)
    entry.delete()
    return redirect('/senior_panel/admin')

@login_required
def delete_header_entry(request, entry_id):
    entry = HeaderEntry.objects.get(pk=entry_id)
    entry.delete()
    return redirect('/senior_panel/admin')

@login_required
def change_user_info(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(request.user.id)

    return redirect('/senior_panel/admin')

@login_required
def logout_view(request):
    return redirect('/accounts/logout')
