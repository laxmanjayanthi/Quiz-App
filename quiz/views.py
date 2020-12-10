from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Question 
# Create your views here.

lst = []*11
anslst= []*11 
answers = Question.objects.all()

for i in answers:
    anslst.append(i.answer)

def welcome(request):
    lst.clear()
    return render(request, 'welcome.html')

def quiz(request):
    obj = Question.objects.all()
    paginator = Paginator(obj, 1)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page=1
    try:
        questions = paginator.page(page)
    except(EmptyPage,InvalidPage):
        questions = paginator.page(paginator.num_pages)
 
    return render(request, 'quiz.html', {'obj':obj,'questions':questions})

def result(request):
    score = 1
    i = 0
    for i in range(len(lst)):
        if lst[i]==anslst[i]:
            score = score + 1
    scr = score>=6
    return render(request, 'result.html',{'score':score, 'scr':scr})  

def saveans(request):
    ans = request.GET['ans']
    lst.append(ans)    


def answers(request):
    obj = Question.objects.all()
    return render(request, 'answers.html', {'obj':obj})     