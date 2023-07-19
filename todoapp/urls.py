from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.create_todo, name='add'),
    path('qrcode/<int:todo_id>/', views.generate_qrcode, name='todo-generate_qrcode'),
]
