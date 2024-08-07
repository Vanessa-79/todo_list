from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *   # Assuming you have a form for handling ToDoItem

# Create your views here.


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


def edit_todo(request, item_id):
    todo_item = get_object_or_404(ToDoItem, id=item_id)
    if request.method == "POST":
        form = ToDoItemForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect("index")  # Redirect to the list view after saving
    else:
        form = ToDoItemForm(instance=todo_item)

        
    return render(request, "edit_todo.html", {"todo_item": todo_item, "form": form})


def delete_todo(request, todo_id):
    todo_item = ToDoItem.objects.get(id=todo_id)
    todo_item.delete()
    return redirect("index")
