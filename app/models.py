# app/models.py
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    # other fields
    def __str__(self) -> str:
        return self.name

class Address(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='address')
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # other fields
    def __str__(self) -> str:
        return self.city

class PhoneNumber(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='phone_numbers')
    number = models.CharField(max_length=20)
    # other fields
    def __str__(self) -> str:
        return self.number
class Interest(models.Model):
    name = models.CharField(max_length=255)
    persons = models.ManyToManyField(Person, related_name='persons')
    # other fields
    def __str__(self) -> str:
        return self.name