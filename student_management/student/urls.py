from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_index, name="student_index"),
    path("student/<int:pk>/", views.student_detail, name="student_detail"),
    path("student/add/", views.student_add, name="student_add"),
    path("student/<int:pk>/edit/", views.student_edit, name="student_edit"),
]