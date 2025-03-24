from django.urls import path

from . import views


urlpatterns = [
    path("", views.TodoView.as_view(), name="TodoView"),
    path("created", views.TodoCreatedView.as_view(), name="TodoCreatedView"),
    path("update/<int:id>", views.TodoUpdateView.as_view(), name="TodoUpdateView"),
    path("delete/<int:id>", views.TodoDeleteView.as_view(), name="TodoDeleteView"),
]
