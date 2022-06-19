from django import forms
from .models import CalendarEntry, Picture, User, UserInfo

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
  header = forms.CharField()
  status = forms.CharField()

  def save(self, user_id):
    if not self.is_valid():
      return

    header = self.cleaned_data.get("header")
    status = self.cleaned_data.get("status")
    print('status: ', status)

    user_info = UserInfo.objects.get(pk=user_id)
    user_info.header = header
    user_info.status = status 
    user_info.save()
