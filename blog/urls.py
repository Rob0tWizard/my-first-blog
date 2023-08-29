from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
#post/ значит, что после начала строки URL должен содержать слово post и косую черту /.
#<int:pk> — означает, что Django ожидает целочисленное значение и преобразует его в представление — переменную pk.
#  / — затем нам нужен еще один символ / перед тем, как адрес закончится.

]

