from audioop import add
from django.urls import path
from todolist.views import delete, show_todolist, status
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import add_todo
from todolist.views import delete
from todolist.views import status


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add/', add_todo, name='add'), 
    path('delete/<int:id>', delete, name='delete'),
    path('status/<int:update_status>', status, name='status'),
]