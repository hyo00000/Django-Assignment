from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo list'

