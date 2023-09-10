from user_auth import views
from django.urls import path,include
from .views import SignUpView

# Created URL to map views from user_auth/views
app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user,
    name='authenticate_user'),
    path("signup/", SignUpView.as_view(), name="signup"),
]
