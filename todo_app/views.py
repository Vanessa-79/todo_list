from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import ToDoItem


def index(request):
    todo_items = ToDoItem.objects.all()
    return render(request, "index.html", {"todo_items": todo_items})


def add_todo(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        ToDoItem.objects.create(title=title, description=description)
        return redirect("index")
    return render(request, "add_todo.html")


def delete_todo(request, todo_id):
    todo_item = ToDoItem.objects.get(id=todo_id)
    todo_item.delete()
    return redirect("index")
