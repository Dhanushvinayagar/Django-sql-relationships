# app/urls.py
from django.urls import path
from .views import (
    PersonListCreateView, PersonRetrieveUpdateDestroyView,
    AddressListCreateView, AddressRetrieveUpdateDestroyView,
    PhoneNumberListCreateView, PhoneNumberRetrieveUpdateDestroyView,
    InterestListCreateView, InterestRetrieveUpdateDestroyView
)

urlpatterns = [
    path('persons/', PersonListCreateView.as_view(), name='person-list-create'),
    path('persons/<int:pk>/', PersonRetrieveUpdateDestroyView.as_view(), name='person-retrieve-update-destroy'),
    path('addresses/', AddressListCreateView.as_view(), name='address-list-create'),
    path('addresses/<int:pk>/', AddressRetrieveUpdateDestroyView.as_view(), name='address-retrieve-update-destroy'),
    path('phone-numbers/', PhoneNumberListCreateView.as_view(), name='phone-number-list-create'),
    path('phone-numbers/<int:pk>/', PhoneNumberRetrieveUpdateDestroyView.as_view(), name='phone-number-retrieve-update-destroy'),
    path('interests/', InterestListCreateView.as_view(), name='interest-list-create'),
    path('interests/<int:pk>/', InterestRetrieveUpdateDestroyView.as_view(), name='interest-retrieve-update-destroy'),
]
