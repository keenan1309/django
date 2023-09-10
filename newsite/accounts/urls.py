from django.urls import path

from .views import SignUpView

# Created a URL pattern for the sign up sheet
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]