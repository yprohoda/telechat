from django.urls import path
from gt import views

urlpatterns = [
    path('register', views.getcaptcha, name='getcaptcha'),
    path('validate', views.validate, name='validate'),
    path('ajax_validate', views.ajax_validate, name='ajax_validate'),
    path('', views.home, name='home')
]

