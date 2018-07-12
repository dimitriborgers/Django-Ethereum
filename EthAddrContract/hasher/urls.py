from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.ContractView.as_view(), name='home'),
]
