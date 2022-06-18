from django.db import models


class User(models.Model):
  username = models.CharField(max_length=200)
  password = models.CharField(max_length=50)
  header = models.CharField(max_length=200)

  def __str__(self):
    return self.username


class Picture(models.Model):
  title = models.CharField(max_length=200)
  img = models.ImageField(upload_to='images/', default=None)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

