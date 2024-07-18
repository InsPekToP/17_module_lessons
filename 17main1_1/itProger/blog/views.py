# from typing import Any
# from django.forms import BaseModelForm
# from django.http import HttpResponse
from django.shortcuts import render
from .models import News
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home2.html'
    context_object_name = 'news'
#св-во сортировки по любому полю кот. есть в табл News
    #ordering = ['id']
    #отбражение от новых к старым (-)
    ordering = ['-date']

    #дополнительные пар-ры:
    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView,self).get_context_data(**kwards)

        ctx['title'] = 'Главная страница сайта'
        return ctx


class NewsDetailView(DetailView):
    model = News
    #template_name = 'blog/news_detail.html'
#можно так или в news_detail.html поменять все post на object
    # context_object_name = 'post'

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView,self).get_context_data(**kwards)

#получаем запись в каждой статье и передаем в заголовок
#не логично,т.к. метод filter берет все статьи,лучше метод get- по
#определенному условию
        #ctx['title'] = News.objects.filter(pk=self.kwargs['pk']).first()
        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx


class UpdateNewsView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title','text']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwards):
        ctx = super(UpdateNewsView,self).get_context_data(**kwards)

        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить статью'
        return ctx
    

    def test_func(self):
#проверяем автора статьи и если он совпадает с залогированым поль-лем,то ок
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False


class DeleteNewsView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = News
#переадресация польз-ля после удаления поста
    success_url = '/'
#пишем каккой шаблон будем вызывать
    template_name = 'blog/delete_news.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False



class CreateNewsView(LoginRequiredMixin,CreateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title','text']

    def form_valid(self, form):
#в качестве автора подставляем того поль-ля,кот был зарегистрирован
        form.instance.avtor = self.request.user
#возвращаем - обращаемся к главному классу и подставляем обновленную форму
        return super().form_valid(form)
    
    def get_context_data(self, **kwards):
        ctx = super(CreateNewsView,self).get_context_data(**kwards)

        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить статью'
        return ctx


def contacti(request):
    return render(request,'blog/contacti.html',{'title': 'Страница контакты1'})

