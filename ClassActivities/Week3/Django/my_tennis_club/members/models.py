from django.db import models

class Member(models.Model):
  username = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)