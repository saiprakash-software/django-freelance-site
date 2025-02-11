from django.urls import path
from .views import signup_view, login_view, logout_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
