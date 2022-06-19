from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  def __str__(self):
    return self.username


class UserInfo(models.Model):
  user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    primary_key=True,
  )
  header = models.CharField(max_length=200)
  status = models.CharField(max_length=200, default='idle')

  def __str__(self):
    return self.user.username


class Picture(models.Model):
  title = models.CharField(max_length=200)
  img = models.ImageField(upload_to='images/', default=None)
  user = models.ForeignKey(User, on_delete=models.CASCADE)


class CalendarEntry(models.Model):
  message = models.CharField(max_length=200)
  date = models.DateField(default=None)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

