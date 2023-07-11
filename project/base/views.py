from django.shortcuts import render, redirect
from .models import  TodoList
from .form import TaskForm
# Create your views here.


def home(request):
    tasks = TodoList.objects.all()

    form = TaskForm()
    high = "High"
    medium = "Medium"
    low = "Low"

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')



    context =  {'tasks': tasks, 'high': high, 'medium': medium, 'low': low, 'form': form}
    return render(request, 'index.html', context)


def done(request, pk):
    obj = TodoList.objects.get(id=pk)
    obj.done = True
    obj.save()

    print(obj.done, obj)
    return redirect('home')

def delete(request, pk):
    obj = TodoList.objects.get(id=pk)
    obj.delete()
    return  redirect('home')