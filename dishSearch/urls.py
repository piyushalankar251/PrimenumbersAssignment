from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search.as_view(), name='search'),
]