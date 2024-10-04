from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.student_index, name="student_index"),
    path("student/<int:pk>/", views.student_detail, name="student_detail"),
    path("student/add/", views.student_add, name="student_add"),
    path("student/<int:pk>/edit/", views.student_edit, name="student_edit"),
    path("student/<int:pk>/delete/", views.student_delete, name="student_delete"),
    path("student/search/", views.student_search, name="student_search"),

    #Authentication
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]