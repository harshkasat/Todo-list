from django.shortcuts import render,HttpResponse, redirect
from .models import Todo
# Create your views here.
def index(request):
    todo = Todo.objects.all()
    if request.method == 'POST':
        new_todo =Todo(
            title = request.POST['title']
        )
        new_todo.save()
        return redirect('/')
    return render(request,'index.html',{'todo':todo})
def delete(request,pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('/')
