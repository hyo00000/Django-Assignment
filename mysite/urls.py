"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from fake_db import user_db

def index(request):
    return HttpResponse('<h1>hello</h1>')

def user_list(request):

    # user_names=[
    #      f'<a href="/name/{user_id}">{user["이름"]}</a>'
    #      for user_id, user in user_db.items()
    # ]
    # response_text = '<br>'.join(user_names)
    # return HttpResponse(response_text)

    return render(request, 'user_list.html', {'users':user_db.items})

def user_info(request, user_id):
    # user = user_db.get(user_id)
    # if user:
    #     details = '<br>'.join([f'{key}:{value}'for key, value in user.items()])
    #     return HttpResponse(details)
    user = user_db.get(user_id)
    return render(request, 'user_info.html',{'user':user})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('users/', user_list, name='user_list'),
    path('name/<int:user_id>/', user_info, name='user_info'),
]
