from .views import index,sign_up,registr,add_user,update_user,delete_user
from django.urls import path

urlpatterns =[
    path('', index, name='index'),
    path('sign_up/',sign_up, name="sign_up"),
    path('registr/',registr, name= 'registr'),
    path('add/user/',add_user,name= 'add_user'),
    path('delete/<int:pk>/',delete_user,name='delete_user'),
    path('update_user/<int:pk>/',update_user,name= 'update_user')    
]