from django.forms import ModelForm
from .models import TodoList

class TaskForm(ModelForm):
    class Meta:
        model = TodoList
        fields = ['task', 'priority']