from django.db import models
from django import forms

# Create your models here.

class Register(models.Model):
    username = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    password1 = forms.CharField(max_length=20)
    password2 = forms.CharField(max_length=20)