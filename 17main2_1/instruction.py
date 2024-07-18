#17main1_1
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

17.39 - надо добавить пару статей