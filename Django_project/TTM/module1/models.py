from django.db import models
# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    class Meta:
        db_table = "Register"
class Feedback(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    phonenumber = models.CharField(max_length=20)
    feedback = models.CharField(max_length=100)
    RATING_CHOICES = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
    rating = models.IntegerField(choices=RATING_CHOICES)
    class Meta:
        db_table = "Feedback"