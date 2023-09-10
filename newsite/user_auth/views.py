from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required



# Create your views here.
# Created function to view the login the page
def user_login(request):
    """Login Page

    Args:
        request (_type_): This will generate the login page

    Returns:
        user_login: this will return the login page requesting username and password
    """
    return render(request, 'authentication/login.html')
# Created function to authenticate the user by fetching the admin info from the database, created to go into login page once logged in.
def authenticate_user(request):

    """This will be to authenticate the user

    Returns:
        This will return the index page if password is incorrect or go through to the homepage
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
        reverse('user_auth:login')
    )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('polls:index')
    )
# Created function for signup view to register
class SignUpView(generic.CreateView):
    """To register a new user

    Args:
        This will return a registration page to register a new user.
    """
    form_class = UserCreationForm
    success_url = reverse_lazy("user_auth:login")
    template_name = "registration/signup.html"


