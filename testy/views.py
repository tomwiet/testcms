from django.shortcuts import render
from django.http import HttpResponse
from testy.models import Question
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'testy/question_list.html',{'questions' :questions})
