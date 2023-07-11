from django.db import models

# Create your models here.

class Priority(models.Model):
    prior = models.CharField(max_length=200)
    color = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.prior


class TodoList(models.Model):
    task = models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, blank=True, null=True, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return  self.task
