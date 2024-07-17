from django.shortcuts import render
#from django.http import HttpResponse
from .models import News

def home(request):
    data = {
        'news': News.objects.all(),
        'title':'Главная страница1'
    }
    return render(request,'blog/home2.html',data)


def contacti(request):
    return render(request,'blog/contacti.html',{'title': 'Страница контакты1'})

