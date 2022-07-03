from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

class User(AbstractUser):
  def __str__(self):
    return self.username

  def save(self, *args, **kwargs):
    is_new = self.id is None
    super(User, self).save(*args, **kwargs)

    if is_new and not self.is_superuser:
      UserInfo.objects.create(user=self)

  def get_sorted_calendar_entries(self, *args, **kwargs):
    now = datetime.datetime.now().date()
    return self.calendarentry_set.all().filter(date__gte=now).order_by('date')[:5]

  def get_status_types(self, *args, **kwargs):
    user_info = UserInfo.objects.get(pk=self)
    return user_info.status_types.split(',')

class UserInfo(models.Model):
  user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    primary_key=True,
  )
  header = models.CharField(max_length=200)
  status = models.CharField(max_length=200, default='idle')
  status_types = models.CharField(max_length=200, default='idle')

  def __str__(self):
    return self.user.username


class HeaderEntry(models.Model):
  message = models.CharField(max_length=200)
  user = models.ForeignKey(User, on_delete=models.CASCADE)


class Picture(models.Model):
  title = models.CharField(max_length=200)
  img = models.ImageField(upload_to='images/', default=None)
  user = models.ForeignKey(User, on_delete=models.CASCADE)


class CalendarEntry(models.Model):
  message = models.CharField(max_length=200)
  date = models.DateField(default=None)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

