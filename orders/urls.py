from django.urls import path
from . import views

urlpatterns = [
  path('table/',views.index3,name='index3'),
   path('order/',views.index2,name='index2'),
]