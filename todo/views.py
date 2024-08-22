
from django.shortcuts import render
from todo.models import Todo
from django.shortcuts import get_object_or_404


def todo(request):
    todo_list = Todo.objects.all()
    context = {'todo_list': todo_list}
    return render(request, 'todo_list.html', context)

def todo_info(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    info = {
        'title': todo.title,
        'description': todo.description,
        'start_date': todo.start_date,
        'end_date': todo.end_date,
        'is_completed': todo.is_completed,
    }
    return render(request, 'todo_info.html', {'data': info})

