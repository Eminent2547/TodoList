from django.contrib import admin
from .models import TodoList, Priority

# Register your models here.

admin.site.register(TodoList)
admin.site.register(Priority)
