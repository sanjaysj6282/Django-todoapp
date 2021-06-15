from django.urls import path,include
from .views import home,todo_list,todo_delete



urlpatterns=[
    path('home',home,name='home'),
    path('all',todo_list,name="all"),
    path('<int:pk>',todo_delete,name='delete')



]