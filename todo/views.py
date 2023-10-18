from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.

def index(request):
    tasks = Todo.objects.all()
    if request.method == 'POST':
        new_todo = Todo(
            title = request.POST['title']
        )
        new_todo.save()
        return redirect('/')
    
    context = {
        'tasks':tasks
    }
    return render(request, 'index.html', context)

def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')