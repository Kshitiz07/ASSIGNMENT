from django.db import models

# define different classes
class Name(models.Model):
    name = models.CharField(max_length=200)

class ID(models.Model):
    id_number = models.IntegerField()

class Contact(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

class Address(models.Model):
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)




