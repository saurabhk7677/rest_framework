from django.db import models

# Create your models here.
class TestCamp(models.Model):
    title = models.CharField(max_length=100)
    mi = models.CharField(max_length=50)
    first = models.CharField(max_length=70)
    last = models.CharField(max_length=70)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    address3 = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone = models.PositiveIntegerField()
    dail_code = models.PositiveIntegerField()
    alt_phone = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)
    show = models.CharField(max_length=100)
    vender_id = models.PositiveIntegerField()
    rank = models.IntegerField()
    owner = models.CharField(max_length=70)
    comments = models.TextField(max_length=300)
