from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),   #без скобок,патому что только обращаемся,выполнять его не надо
    path('about',views.about,name='about'),
    path('contacts',views.contacts,name='contacts')
]