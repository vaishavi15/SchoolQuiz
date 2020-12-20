
from django.http import HttpResponse
import json as simplejson
from django.shortcuts import render
import requests


def index(request):
    return render(request,'quizes.html')

def quizzes(request):
    apiapi='https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple'
    quiz='Quiz_app'

    PARAMS={'results':quiz}

    info=requests.get(url=apiapi)


    data=info.json()

    questions=[]
    qa=[]
    qia=[]
    qandaa={}
    for any in data['results']:
        questions.append(any['question'])
        qa.append(any['correct_answer'])
        qia.append(any['incorrect_answers'])
        qandaa.update({any['question']:any['correct_answer']})
    
    return render(request,'quiz.html',{'questions':questions,'qanda':qa,'qandia':qia,'data':data,'qanda1':qandaa})

def results(request):
    return render(request,'result.html')