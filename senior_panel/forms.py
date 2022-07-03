from django import forms
from .models import CalendarEntry, Picture, User, UserInfo, HeaderEntry

class PictureForm(forms.Form):
  title = forms.CharField()
  image = forms.ImageField()

  def save(self, user_id):
    if not self.is_valid():
      return

    title = self.cleaned_data.get("title")
    img = self.cleaned_data.get("image")
    user = User.objects.get(pk=user_id)
    obj = Picture.objects.create(title = title, img = img, user = user)
    obj.save()

class CalendarEntryForm(forms.Form):
  message = forms.CharField()
  date = forms.DateField()

  def save(self, user_id):
    if not self.is_valid():
      return

    message = self.cleaned_data.get("message")
    date = self.cleaned_data.get("date")

    user = User.objects.get(pk=user_id)
    obj = CalendarEntry.objects.create(message = message, date = date, user = user)
    obj.save()

class UserInfoForm(forms.Form):
  status_types = forms.CharField()

  def save(self, user_id):
    if not self.is_valid():
      return

    status_types = self.cleaned_data.get("status_types")

    user_info = UserInfo.objects.get(pk=user_id)
    user_info.status_types = status_types 
    user_info.save()

class HeaderEntryForm(forms.Form):
  message = forms.CharField()

  def save(self, user_id):
    if not self.is_valid():
      return

    message = self.cleaned_data.get("message")

    user = User.objects.get(pk=user_id)
    obj = HeaderEntry.objects.create(message = message, user = user)
    obj.save()
