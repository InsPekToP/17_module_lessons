#17main2_1
#Постраничный вывод статей

#Сделаем чтобы в статьях отображался HTML код
#<p>{{post.text|striptags}}</p> - фильтр,не показывает HTML-код
#|truncatechars:200 - показывает 200 символов
#|safe - обрабатывается HTML

#создаем пагинацию в views.py в ShowNewsView добавляем paginate_by = 2
#http://127.0.0.1:8000/?page=2 - теперь работает,и нужно добавить кнопки
#перехода
# проверка на наличие пред страницы
#       {% if page_obj.has_previous %}
#          <a href="{% url 'home' %}" class="btn btn-outline-danger">Начало</a>
#          <a href="?page={{ page_obj.previous_page_number }}" class="btn btn-outline-danger">Предыдущая</a>
#       {% endif %}

#теперь между кнопками выводим цифры(но не все)
#{% for num in page_obj.paginator.page_range
#  
#elif num > page_obj.number|add:'-3' %}--обьяснение:
#предположим,сто мы находимся на 5й странице--тогда
#в цикле мы доходим до 2й странице,и если 2 будет больше 5'-3" то 
#делаем что-то.Тогда если мы на 3й странице,то условие будет верно т.к. 3>(5-3)

#делаем страницу автора
#в views.py(blog) from django.shortcuts import  get_object_or_404
#from django.contrib.auth.models import User
#делаем новый шаблон template_name = 'blog/user_news.html'
#переписываем SQL-запрос,т.к. сейчас будет показываться все записи из табл News
#def get_queryset():
#теперь делаем шаблон user_news.html копируем все из home2.html

#и плюс делаем ссылки на авторов в home2.html

#поменяем титул страницы про автора
#в views.py ctx['title'] = 'Главная страница сайта' --- 
#--- ctx['title'] = f'Статьи от пользователя {self.kwargs.get('username')}'