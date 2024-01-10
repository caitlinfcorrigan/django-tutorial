from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # create context var to hold object with req vars
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def details(request, question_id):
    # Instead of try/except, use Django shortcut to throw 404 if resource (survey) does not exist
    # First arg is Model, then kwargs
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)