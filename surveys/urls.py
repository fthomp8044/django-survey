from django.urls import path
from . import views

# dont forget the app_name. it helps refer to the name for url
app_name= 'surveys'

urlpatterns = [
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('', views.IndexView.as_view(), name='index'),
    path('new/', views.CreateView.as_view(), name='create'),
]
