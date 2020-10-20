from django.db import models
from django.contrib.auth.models import User


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=15, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    id_no = models.CharField(max_length=30, null=True, blank=True)


class book_details(models.Model):
    book_no = models.IntegerField()
    book_name = models.TextField()
    btd = models.DateField()
    bsd = models.DateField(null=True, blank=True)
    uname = models.TextField()
    email = models.EmailField(null=True)
    uid = models.CharField(max_length=20)
    fine = models.FloatField(null=True, blank=True)
    status = models.BooleanField(default=0)