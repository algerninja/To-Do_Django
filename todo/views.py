import datetime
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from todo.forms import TodoForm
from todo.models import ToDoItem
from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
@method_decorator(csrf_exempt, name="dispatch")
class TodoView(LoginRequiredMixin, View):
    login_url = "/auth/login/"
    redirect_field_name = "redirect_to"

    def get(self, request):
        todoItems = ToDoItem.objects.all()
        form = TodoForm()
        return render(
            request,
            "todo.html",
            context={"method": "get", "form": form, "items": todoItems},
        )

    def post(self, request):
        form = TodoForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            data["created_at"] = datetime.datetime.now()
            todoItem = ToDoItem(**data)
            todoItem.save()

        return redirect("TodoView")


@method_decorator(csrf_exempt, name="dispatch")
class TodoCreatedView(LoginRequiredMixin, View):
    login_url = "/auth/login/"
    redirect_field_name = "redirect_to"

    def get(self, request):
        todoItems = ToDoItem.objects.all()
        form = TodoForm()
        return render(
            request,
            "todoForm.html",
            context={"method": "get", "form": form, "items": todoItems},
        )

    def post(self, request):
        form = TodoForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            data["created_at"] = datetime.datetime.now()
            todoItem = ToDoItem(**data)
            todoItem.save()

        return redirect("TodoView")


@method_decorator(csrf_exempt, name="dispatch")
class TodoUpdateView(LoginRequiredMixin, View):
    login_url = "/auth/login/"
    redirect_field_name = "redirect_to"

    def get(self, request, id):
        if not id:
            print("❌ id is required")
            return redirect("TodoView")

        try:
            todoItems = ToDoItem.objects.get(id=id)

        except Exception as e:
            print("Item not found")
            return redirect("TodoView")

        form = TodoForm(
            data={
                "title": todoItems.title,
                "description": todoItems.description,
                "completed": todoItems.completed,
            }
        )

        return render(
            request,
            "todoForm.html",
            context={"method": "get", "form": form, "items": todoItems},
        )

    def post(self, request, id):
        form = TodoForm(request.POST or None)

        if form.is_valid():
            obj = get_object_or_404(ToDoItem, id=id)
            data = form.cleaned_data
            data["update_at"] = datetime.datetime.now()

            obj.title = data["title"]
            obj.description = data["description"]
            obj.completed = data["completed"]
            obj.update_at = data["update_at"]
            obj.save()

        return redirect("TodoView")


class TodoDeleteView(LoginRequiredMixin, View):
    login_url = "/auth/login/"
    redirect_field_name = "redirect_to"

    def get(self, request, id):
        try:
            todoItems = get_object_or_404(ToDoItem, id=id)
        except Exception as e:
            return redirect("TodoView")

        todoItems.delete()
        return redirect("TodoView")
