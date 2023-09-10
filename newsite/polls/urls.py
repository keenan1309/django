from django.urls import path,include
from . import views

# Mapped the path for polls and functions  associated with the app and webpage
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
]
