from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Questions, Choice

def index(request):
    latest_question_list = Questions.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list" : latest_question_list,
    }
    return HttpResponse(template.render(context=context, request=request))


def details(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    template = loader.get_template("polls/details.html")
    context = {
        "question" : question,
    }
    return HttpResponse(template.render(context=context, request=request))



def results(request, question_id):
    return HttpResponse("You are looking at the result of question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)


