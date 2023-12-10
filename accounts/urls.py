from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup_view, name='signup'),
    path('', views.index, name='index'),

    # path('login', views.login_view, name='login'),
]