from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question
from django.contrib.auth.decorators import login_required
# Create your views here.

# Made login a requirement using the import login required
@login_required()
#Created the functions with attributes to link to the template this will show the question of the vote
def index(request):
    """The index function to return articles list

    Args:
        request (index): This function renders the object view to see articles within a list format.

    Returns:
        This returns a list format of all the articles we have loaded in the database.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
#Created the functions with attributes to link to the template this will show the question and choices of the vote
def detail(request, question_id):
    """The will return the object requested from the list and return in a detailed format

    Args:
        request (index): This uses the question ID as PK and returns the value from sqlite3 database

    Returns:
        This gets a specific item selected by the user and returns the full article.
    """
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
