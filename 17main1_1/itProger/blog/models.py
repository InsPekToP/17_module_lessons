from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#Табличка
class News(models.Model):
    title = models.CharField('Название статьи',max_length=100,unique=True)
    #unique=True - нельзя создать две статьи с одинаковым названием
    text = models.TextField('Основной текст статьи')
    date = models.DateTimeField('Дата',default=timezone.now)
    #здесь прописали,что если удаляем польз-ля,то и удаляем все его посты
    #on_delete=None(не удаляем)(on_delete=models.CASCADE) - удаляем
    #avtor - поле кот. привязано к опр. автору в табличке поль-ли(User)
    avtor = models.ForeignKey(User,verbose_name='Автор',on_delete=models.CASCADE)

#существуют и другие поля
    views = models.IntegerField('Просмотры',default=1)
    #views2 = models.FloatField('Просмотры',default=1) - числа с точкой
    # sizes = (
    #     ('S', 'Small'),
    #     ('M', 'Medium'),
    #     ('L', 'Large'),
    #     ('XL', 'X large'),
    # )
    # shop_sizes = models.CharField(verbose_name='Размер',max_length=2,choices=sizes,default='S')

#исправляем News object (1)
    def __str__(self):
        return f'{self.title}'

#пишем название таблички в одиночном числе
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'