from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('my_profile/', views.my_profile, name='my_profile'),
    path("login/", views.login, name="login"),
    path("login_dj/", auth_views.LoginView.as_view(template_name='login.html'), name="loginTT"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("social-auth/", include('social_django.urls', namespace="social")),
]