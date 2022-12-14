from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import datetime
import json

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user) # get model data
   # apapun yang mau di akses di template, harus taro di context
    context = {
    'list_todo': data_todolist,
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def add_todo(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.now()
        is_finished = False
        Task.objects.create(title=title, description=description, date=date, user=request.user, is_finished=is_finished)
        response = HttpResponseRedirect(reverse('todolist:show_todolist'))
        return response
    return render(request, "add_todo.html")

def delete_task(request, id):
    data = Task.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

def status_task(request, update_status):
    data_status = Task.objects.get(id=update_status)
    if data_status.is_finished == False:
        data_status.is_finished = True
    else:
        data_status.is_finished = False
    data_status.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

@login_required(login_url='/todolist/login/')
def show_json(request):
    task = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', task), content_type='application/json')

def add_task_ajax(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        add_todolist = Task(
            user = request.user,
            title = title,
            description = description,
            date = datetime.datetime.now(),
            is_finished = False,
        )
        add_todolist.save()
    return JsonResponse({"task": "todolist baru"},status=200)

@csrf_exempt
def delete_task_ajax(request,id):
    task = Task.objects.filter(pk=id)   
    task.delete()
    return JsonResponse({"task": "todolist dihapus"})