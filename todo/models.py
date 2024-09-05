from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'[{self.get_category_display()}] {self.title[:10]}'

    def get_absolute_url(self):
        return reverse('todo:info', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo list'

