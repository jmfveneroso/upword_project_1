from django import forms
from .models import Picture, User

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
