from django.urls import path

from todo import views

app_name = 'fb'
# #FBV todo
urlpatterns = [
    path('', views.todo, name='list'),
    path('<int:pk>/', views.todo_info, name='info'),
    path('create/', views.todo_create, name='create'),
    path('<int:pk>/update/', views.todo_update, name='update'),
    path('<int:pk>/delete', views.todo_delete, name='delete'),

]