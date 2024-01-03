# app/serializers.py
from rest_framework import serializers
from .models import Person, Address, PhoneNumber, Interest


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'


class InterestSerializer(serializers.ModelSerializer):
    persons = serializers.PrimaryKeyRelatedField(many=True, queryset=Person.objects.all())
    class Meta:
        model = Interest
        fields = '__all__'

class InterestViewSerializer(serializers.ModelSerializer):
    persons = PersonSerializer(many=True)
    class Meta:
        model = Interest
        fields = '__all__'