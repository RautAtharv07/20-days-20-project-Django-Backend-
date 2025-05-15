from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import Quize,question
from .forms import quizeForm,questionForm

# Create your views here.

def home(request):
    return render(request,'home.html')

def UserLogin(request):
    if request.method== 'POST':
        form = AuthenticationForm(request,data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
        else:
            print("helloworld")
    else:
        form =AuthenticationForm()
    return render(request,'login.html',{'form':form})

def SignUp(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})

def User_logout(request):
    logout(request)
    return redirect('home')

def create_quize(request):
    if request.method=="POST":
        form = quizeForm(request.POST)
        if form.is_valid():
            quiz = form.save()
            return redirect('quizehome',quizeid=quiz.id)
    else:
        form = quizeForm()
    return render(request,'createquize.html',{'form':form})

def quizehome(request, quizeid):
    quize = get_object_or_404(Quize, id=quizeid)
    questions = question.objects.filter(quize=quize)
    return render(request, 'quizehome.html', {'quize': quize, 'questions': questions})

def add_question(request,quizeid):
    quize = get_object_or_404(Quize,id=quizeid)
    if request.method=='POST':
        form = questionForm(request.POST)
        if form.is_valid():
            que = form.save(commit=False)
            que.quize = quize
            que.save()
            return redirect('quizehome', quizeid=quize.id)

    else:
        form = questionForm()
    return render(request,'addquestion.html',{'form':form,'quiz':quize})
@login_required
def dashboard(request):
    quizes = Quize.objects.all()
    return render(request,'dashboard.html',{"quizes":quizes})

def deletequiz(request,quizeid):
    quiz = get_object_or_404(Quize,id = quizeid)
    quiz.delete()
    return redirect('dashboard')

def takequiz(request,quize_uuid):
    quiz = get_object_or_404(Quize,uuid = quize_uuid)
    questions = quiz.questions.all()
    if request.method=="POST":
        return redirect('submit_quiz',quize_uuid)
    return render(request ,'takequiz.html',{'quiz':quiz,'questions':questions})

def sharequiz(request,quize_uuid):
    quiz = get_object_or_404(Quize,uuid=quize_uuid)
    return render(request,'sharequiz.html',{'quiz':quiz})


def submit_quiz(request,quize_uuid):
    quiz = get_object_or_404(Quize,uuid=quize_uuid)
    questions = quiz.questions.all()
    
    if request.method =="POST":
        count =0
        total = questions.count()
        
        for q in questions:
            user_answer = request.POST.get(f"q{q.id}")
            correct_option_field = q.correct
            correct_answer = getattr(q, correct_option_field)

            print(f"Question: {q.text}")
            print(f"User Answer: {user_answer}")
            print(f"Correct Option Field: {correct_option_field}")
            print(f"Correct Answer Text: {correct_answer}")
            if correct_answer == user_answer:
                count+=1

        context = {
            'quiz': quiz,
            'score': count,
            'total': total,
        }
        return render(request, 'score.html', context)
    return render(request,'takequiz.html',{'quiz':quiz,'questions':questions})
    