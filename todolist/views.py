from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

# Create your views here.
def todoview(request):
    all_todo=TodoItem.objects.all()
    return render(request, 'todo/todo.html',
                {'all_list':all_todo})

def addTodo(request):
    #c = request.POST['filed']
    new_item = TodoItem(field = request.POST['filed'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request,todo_id):
    item_del=TodoItem.objects.get(id=todo_id)
    item_del.delete()
    return HttpResponseRedirect('/todo/')
    

