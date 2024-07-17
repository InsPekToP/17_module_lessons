from typing import Any
from django.shortcuts import render
from .models import News
from django.views.generic import ListView



def home(request):
    data = {
        'news': News.objects.all(),
        'title':'Главная страница!'
    }
    return render(request,'blog/home2.html',data)


class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home2.html'
    context_object_name = 'news'
#св-во сортировки по любому полю кот. есть в табл News
    #ordering = ['id']
    ordering = ['date']

    #дополнительные пар-ры:
    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView,self).get_context_data(**kwards)

        ctx['title'] = 'Главная страница сайта'
        return ctx

def contacti(request):
    return render(request,'blog/contacti.html',{'title': 'Страница контакты1'})

