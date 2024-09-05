from datetime import timedelta, datetime

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from todo.forms import TodoForm
from todo.models import Todo
from django.shortcuts import get_object_or_404


def todo(request):
    todo_list = Todo.objects.all()

    q = request.GET.get('q')
    if q:
        todo_list = todo_list.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q)
        )
        

    paginator = Paginator(todo_list, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'object_list': page_obj.object_list,
        'page_obj': page_obj,
    }
    return render(request, 'todo_list.html', context)

def todo_info(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    context = {
        'todo': todo,
    }
    return render(request, 'todo_info.html', context)

@login_required()
def todo_create(request):
    # if not request.user.is_authenticated:
    #     return redirect(reverse('login'))

    form = TodoForm(request.POST or None)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.author = request.user
        todo.save()
        return redirect(reverse('fb:info', kwargs={'pk':todo.pk}))

    context = {
        'form': form
    }
    return render(request,'todo_create.html', context)

@login_required()
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk, author=request.user)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.modified_at= datetime.now()
        todo.save()
        return redirect(reverse('fb:info', kwargs={'pk': todo.pk}))

    context = {
        'todo': todo,
        'form': form,
    }
    return render(request,'todo_update.html', context)

@login_required()
@require_http_methods(['POST'])
def todo_delete(request, pk):
    # if request.method != 'POST':
    #     raise Http404

    todo = get_object_or_404(Todo, pk=pk, author=request.user)
    todo.delete()

    return redirect(reverse('fb:list'))