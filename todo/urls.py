from django.urls import path
from . import views
urlpatterns = [

    path('', views.todolist,name='todolist'),   
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('delete/<task_id>', views.delete_task,name='delete_task'),
    path('edit/<task_id>', views.edit_task,name='edit_task'),
 	path('complete/<task_id>', views.complete_task,name='complete_task'),
 	path('pend/<task_id>', views.pend_task,name='pend_task'),
 ]