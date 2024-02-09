# urls.py in tadwin22 app

from django.urls import path
from . import views
from .views import login_view

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('loggedin/', views.loggedin_view, name='loggedin'),
    path('login_form/', views.login_form, name='login_form'),

    # Add other URLs specific to the app here
]
