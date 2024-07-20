#17main4_1
#Публикация сайта на сервер

#проверка на наличие Heroku -- heroku прописать в терминале 
#для логина -- heroku login
#дальше любую клавишу или q - для выхода.
#pip install gunicorn
#создаем requirements.txt
#pip freeze
#pip freeze >requirements.txt
#надо перекинуть в папку с проектом
#дальше git init --и commit и добавить gitignore и commit 
#https://github.com/github/gitignore/blob/main/Python.gitignore

#если работаем на Mac добавляем .DC_Store
#создаем приложение на heroku.com

#heroku create itproger-django-blog-test1

#https://itproger-django-blog-test1-0147da1c30a5.herokuapp.com/ |
#  https://git.heroku.com/itproger-django-blog-test1.git

#поменять адресс,надо купить подписку
#heroku open - открыть в браузере
#git push heroku master

#выбивает ошибку из- за статических файлов
#  ! [remote rejected] master -> master (pre-receive hook declined)
# error: failed to push some refs to 'https://git.heroku.com/inspektop-django-blog-test2.git'
#надо указать STATIC_ROOT в settings.py 
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#проводим commit и выгружаем на heroku
#git commit -m "modified settings.py"
#git push heroku master
#heroku open

#выбивает следующую ошибку Application error,но уже на сайте
#чтобы узнать какая ошибка heroku logs --tail
#at=error code=H14 desc="No web processes running" -- нет какого-то веб процесса
#создаем файл Procfile и прописываем web: gunicorn itProger.wsgi

#выбивает следующую ошибку уже от django Invalid HTTP_HOST header:
#  'inspektop-django-blog-test2-e725fef9190b.herokuapp.com'. 
# You may need to add 'inspektop-django-blog-test2-e725fef9190b.herokuapp.com' to ALLOWED_HOSTS.
#значение DEBUG надо установить со значением False(но это потом)
#сейчас же нам надо в ALLOWED_HOSTS добавить inspektop-django-blog-test2-e725fef9190b.herokuapp.com
#тоесть в разрешенные ХОСТЫ добавить наш сайт
#ALLOWED_HOSTS = ['inspektop-django-blog-test2-e725fef9190b.herokuapp.com'] в settings.py

#новая ошибка:нет такой таблички как blog_news
#OperationalError at /
#no such table: blog_news
#в игнор файлы добавили sqlite3,поэтому у нас сейчас нет БД
#нам нужно указать что будем исп-ть PostgreSQL(она уже включена в Heroku)

#heroku addons - команда позволяет посмотреть есть ли БД подключенная к проекту
#heroku addons:create heroku postgresql:hobby-dev - подключить БД
#heroku pg - хар-ки БД
#не работает бесплатно пришлось подключить
#heroku addons:create heroku-postgresql:essential-0

#чтобы добавить таблички,надо провести миграции.
#Для этого устанавливаем библиотеку 
#pip install django-heroku
#дальше import django_heroku в settings.py
#django_heroku.settings(locals()) - теперь та БД,что была в проекте
#совместима с той,что есть в heroku

#теперь надо обновить requirements.txt
#pip freeze > requirements.txt

#теперь надо провести миграции и создать суперюзера для админ-панели
#heroku run - позволяет запустить другую команду на стороне приложения?
#heroku run python manage.py migrate

#создаем супер пользователя
#heroku run bash запускает терминал на стороне heroku
#прописываем команды как на Linux
#ls
#python manage.py createsuperuser
#exit - выход

#при покупке домена надо будет работать с DNS-серверами
#https://devcenter.heroku.com/articles/custom-domains