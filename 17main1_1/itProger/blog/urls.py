from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home, name='home'),
    path('',views.ShowNewsView.as_view(), name='home'),
    path('about',views.contacti, name='contacti')
]