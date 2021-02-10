from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import  Tasklist
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
def todolist(request):
	if request.method == "POST":
		form = TaskForm(request.POST or None)
		if form.is_valid():
			form.save()
		messages.success(request,("New Task Added!"))	
		return redirect('todolist')	
	else:
		all_tasks = Tasklist.objects.all()
		paginator = Paginator(all_tasks, 5)
		page = request.GET.get('pg')
		all_tasks = paginator.get_page(page)
		return render(request,'todolist.html',{'all_tasks': all_tasks})


def delete_task(request,task_id):
	task = Tasklist.objects.get(pk=task_id)
	task.delete()
	return redirect('todolist')


def edit_task(request,task_id):
	if request.method == "POST":
		task = Tasklist.objects.get(pk=task_id)
		form = TaskForm(request.POST or None, instance = task)
		if form.is_valid():
			form.save()
		messages.success(request,("Task Edited!"))	
		return redirect('todolist')	
	else:
		ctx = {
		'task_object':Tasklist.objects.get(pk=task_id)
		}
		return render(request,'edit.html',ctx)



def about(request):
	ctx = {
	'about_text': 'Welcome About Us page!'
	}
	return render(request,'about.html',ctx)

def contact(request):
	ctx = {
	'contact_text': 'Welcome Contact page!'
	}
	return render(request,'contact.html',ctx)

def complete_task(request,task_id):
	task = Tasklist.objects.get(pk=task_id)
	task.done = True
	task.save()
	return redirect('todolist')

def pend_task(request,task_id):
	task = Tasklist.objects.get(pk=task_id)
	task.done = False
	task.save()
	return redirect('todolist')	


def index(request):
	ctx = {
	'about_text': 'Welcome About Us page!'
	}
	return render(request,'index.html',ctx)