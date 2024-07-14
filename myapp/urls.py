
from django.urls import path
from . import views

urlpatterns = [
    path('email/', views.email_form, name='about'),

]
