#17main3_1
#Кнопка востановления пароля

#в urls.py прописываем отслеживание
#path('pass-reset/',authViews.PasswordResetView.as_view
# (template_name = 'users/pass_reset.html'), name='pass-reset'),
#далее делаем шаблон и копируем из user.html
#далее выбивает ошибку Обратное значение для «password_reset_confirm» не найдено.
#«password_reset_confirm»  - не отслеживается 
#надо прописать отслеживание такого адреса:
#{{ protocol }}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}
#тоесть
#http://127.0.0.1:8000/password_reset_confirm/<uidb>/<token>

#делаем еще 2 шаблона password_reset_confirm.html и password_reset_done.html
#и опять выбивает ошибку
#надо дописать за счет какого почтового клиета будем отправлять емейлы в settings.py
#с локальным сервером может не работать
#прописываем данные для работы с GMAIL.com

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
#с какого емейла отправляться будет почта
# EMAIL_HOST = 'inspektop1@gmail.com.com'
# EMAIL_HOST_PASSWORD = ''

#выбивает новая ошибка
#ищем google app pasword заходим https://myaccount.google.com/
#и делаем пароль на приложение ПОЧТА 
#и копируем в EMAIL_HOST_PASSWORD = ''

#создаем новое отслеживание
#эту страничку будем показывать в самую последнюю очередь
    # path('password_reset_complete/',
    #      authViews.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'),
    #       name='password_reset_complete'),
#перекидываем в него шаблон из password_reset_done.html

#теперь в urls.py делаем ссылку