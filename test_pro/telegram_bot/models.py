from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=56, null=True)
    surname = models.CharField(max_length=56, null=True)
    phone_number = models.CharField(max_length=56, null=True)


class Log(models.Model):
    user_id = models.IntegerField(primary_key=True)
    log = models.JSONField()


