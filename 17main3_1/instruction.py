#17main1_1
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