from app1.views import *
from django.urls import path
app_name='somthing'
urlpatterns=[
    path('pspk/',pspk,name='pspk'),
]