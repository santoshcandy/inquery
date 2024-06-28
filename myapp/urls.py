from django.urls import path
from . import views

urlpatterns=[
    path('api/contacts/',views.get_contacts,name='get_contacts'),
    path('',views.index,name='index')
]