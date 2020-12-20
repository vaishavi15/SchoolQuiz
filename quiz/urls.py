
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('quizzes/',views.quizzes,name='quiz'),
    path('quizzes/result/',views.results,name='result'),
    
     

]