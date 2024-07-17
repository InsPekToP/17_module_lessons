#17main1_1
#Добавление и удаление постов

#переписываем ф-ию home в файле views.py
#from django.views.generic import ListView
#в urls.py пишем path('',views.ShowNewsView.as_view(), name='home'),
#выбивает ошибку TemplateDoesNotExist at / blog/news_list.html
#чтобы устранить:class ShowNewsView(ListView):
#     model = News,
#     template_name = 'blog/home2.html'

9.53