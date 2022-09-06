from distutils.command.upload import upload
from operator import mod
from statistics import mode
from django.db import models


class Post(models.Model):
    image = models.ImageField(upload_to='YouTube.IM/%Y/%m')


# Create your models here.
