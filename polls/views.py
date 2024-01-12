from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
# To avoid hardcoding the redirect url
from django.urls import reverse

from .models import Question, Choice


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     # create context var to hold object with req vars
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)

# def details(request, question_id):
#     # Instead of try/except, use Django shortcut to throw 404 if resource (survey) does not exist
#     # First arg is Model, then kwargs
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {"question": question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:

        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        request, 'polls/detail.html', {
            "question": question,
            "error_message": "You didn't select a choice."
        }
    else:
        selected_choice.votes += 1
        selected_choice.save()
    # Always return HttpResponseRedirect after successfully POST-ing to prevent data from posting twice if user hits Back button
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # Reverse url retruns string like /polls/3/results

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # Return last 5 questions
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model = Question
    # Default template name is <app name>/<model name>_detail.html
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'