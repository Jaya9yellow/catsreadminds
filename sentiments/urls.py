from django.urls import path

from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('senti',views.senti, name='senti')
   
]


 