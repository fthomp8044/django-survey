from django.urls import path
from . import views

# dont forget the app_name. it helps refer to the name for url
app_name= 'tools'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),



]
