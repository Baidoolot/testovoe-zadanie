from django.urls import path
from .views import GetQuestion, QuestionAnswer

app_name = 'quiz'

urlpatterns = [
    path('', GetQuestion.as_view()),
    path('answer/', QuestionAnswer.as_view()),
]