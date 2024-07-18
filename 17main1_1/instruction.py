#17main1_1
#Добавление и удаление постов

#переписываем ф-ию home в файле views.py
#from django.views.generic import ListView
#в urls.py пишем path('',views.ShowNewsView.as_view(), name='home'),
#выбивает ошибку TemplateDoesNotExist at / blog/news_list.html
#чтобы устранить:class ShowNewsView(ListView):
#     model = News,
#     template_name = 'blog/home2.html'

#http://127.0.0.1:8000/news/1...4 хотим создать отображение страниц
#в папке views.py импорт класса DetailView

#path('news/<int:pk>',views.ShowNewsView.as_view(), name='home'),
#настраиваем отслеживание динамического адресса
#/<slug: - строка,int:- число
#<int:pk - первичный ключ(без пробелов)

#template_name = 'blog/news_detail.html' - если это убрать,то по умолчанию
#будет подставляться тот же шаблон 
#news - модель,detail - название класса (DetailView)

#делаем кнопки в home2.html

#получаем запись в каждой статье и передаем в заголовок в views.py
#(**kwards) и kwargs - разные значения

#создаем страницу с формочкой,чтобы добавлять статью в базу данных в views.py
#импорт CreateView class CreateNewsView(CreateView):

#при добавлении статьи выбивает ошибку - по умолчанию стоят значения везде кроме avtor
#Не удалось выполнить ограничение NOT NULL: blog_news.avtor_id
#исправляем добавляя класс для отслеживания def form_valid(self, form):

#опять выбивает ошибку
#Нет URL для перенаправления. Укажите URL или определите метод get_absolute_url в модели.
#исправить: в models.py from django.urls import reverse
#и дописать ф-ию    def get_absolute_url(self):
        #return reverse('news-detail',kwargs={'pk': self.pk})

#теперь http://127.0.0.1:8000/news/add доступна всем польз-лям
#в views.py from django.contrib.auth.mixins import LoginRequiredMixin
#--только зареганые польз-ли могли видеть эту страницу
#class CreateNewsView(LoginRequiredMixin,CreateView): - обновили класс

#страница с обновлением статьи
#import UpdateView class UpdateNewsView(LoginRequiredMixin,UpdateView):
#def get_context_data(self, **kwards): - дописываем доп. пар-ры в зависимости
#на какой странице мы находимся
        # ctx['title'] = 'Обновление статьи'
        # ctx['btn_text'] = 'Обнивить статью'
        # return ctx
#и тоже самое в CreateNewsView

#теперь кто угодно может обновить любую статью(и станет автором этой статьи)
#from django.contrib.auth.mixins import UserPassesTestMixin
#и в class UpdateNewsView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
#дописываем:
    #def test_func(self):
#проверяем автора статьи и если он совпадает с залогированым поль-лем,то ок
        # news = self.get_object()
        # if self.request.user == news.avtor:
        #     return True
        # return False

#удалить статью(если она наша)
#from django.views.generic import DeleteView
#class DeleteNewsView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
#переадресация польз-ля после удаления поста
    #success_url = '/'
#в urls.py --path('news/<int:pk>/delete',views.DeleteNewsView.as_view(), name='news-delete')

#и добавляем ссылки в base.html
     # <a href="{% url 'news-add' %}" class="ml-2">
     #   <button class="btn btn-outline-secondary">Добавить статью</button>
     # </a>

        #  {% if object.avtor == user %}
        #  <hr>
        #  <a href="{% url 'news-update' object.id %}" class="btn btn-info">Обновить статью</a>
        #  <a href="{% url 'news-delete' object.id %}" class="btn btn-danger">Удалить статью</a>
        #  {% endif %}