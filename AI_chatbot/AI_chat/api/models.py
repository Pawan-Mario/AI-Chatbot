from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User

# Create your models here.


class CodeExplainer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    _input = models.TextField()
    _output = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "t_code_explainer"

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    tokens = models.IntegerField(default=4000)

