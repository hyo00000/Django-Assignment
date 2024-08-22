from django.contrib import admin
from todo.models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','is_completed']
    list_display_links = ['id']
    list_filter = ['id','title']


admin.site.register(Todo, TodoAdmin)