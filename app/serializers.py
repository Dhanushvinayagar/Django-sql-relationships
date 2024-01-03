# app/serializers.py
from rest_framework import serializers
from .models import Person, Address, PhoneNumber, Interest


class PersonSerializer(serializers.ModelSerializer):
    interests = serializers.PrimaryKeyRelatedField(many=True, queryset=Interest.objects.all())

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
    class Meta:
        model = Interest
        fields = '__all__'


#   View only (get method only supported to view complete data from many to many)
class PersonViewSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(many=True)
    class Meta:
        model = Person
        fields = '__all__'