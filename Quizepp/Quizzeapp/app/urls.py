from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('login/', UserLogin, name='login'),
    path('logout/', User_logout, name='logout'),
    path('register/', SignUp, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('quizehome/<int:quizeid>/', quizehome, name='quizehome'),
    path('create_quize/', create_quize, name='create_quize'),
    path('add_question/<int:quizeid>/', add_question, name='add_question'),  
    path('deletequiz/<int:quizeid>/',deletequiz,name='deletequiz'),
    path('takequize/<uuid:quize_uuid>/',takequiz,name='takequiz'),
    path('sharequiz/<uuid:quize_uuid>/',sharequiz,name='sharequiz'),
    path('submitquiz/<uuid:quize_uuid>/', submit_quiz, name='submit_quiz'),

]
