from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

def index(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    return render(request, 'my_app/index.html', context={'todo_items':todo_items})

@csrf_exempt
def add_todo(request):
    todo_text = request.POST.get('input')
    if todo_text.strip() != '':
        Todo.objects.create(text=todo_text.title(), added_date=timezone.now())
    return HttpResponseRedirect("/")
    
@csrf_exempt
def delete_todo(request, item_pk):
    Todo.objects.get(pk=item_pk).delete()
    return HttpResponseRedirect('/')