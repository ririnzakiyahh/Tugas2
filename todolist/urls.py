from audioop import add
from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import add_todo
from todolist.views import delete_task
from todolist.views import status_task
from todolist.views import show_json
from todolist.views import add_task_ajax
from todolist.views import delete_task_ajax



app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add/', add_todo, name='add'), 
    path('delete_task/<int:id>/', delete_task , name='delete_task'),
    path('status_task/<int:update_status>/', status_task, name='status_task'),
    path('json/', show_json, name='show_json'),
    path('add_task_ajax/', add_task_ajax, name='add_task_ajax'),
    path('delete/<int:id>/', delete_task_ajax, name='delete_task_ajax'),
]