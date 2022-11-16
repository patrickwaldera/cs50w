
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),

    path("home", views.home, name="home"),
    path("passwords", views.passwords, name="passwords"),
    path("notes", views.notes, name="notes"),
    path("generator", views.generator, name="generator"),
    path("new", views.new, name="new"),

    path("api/notes", views.notes_api, name="notes_api"),
    path("api/passwords", views.passwords_api, name="passwords_api"),
    path("api/allitens", views.allitens, name="allitens"),
    path("api/notes/edit/<int:id>", views.notes_edit, name="notes_edit"),
    path("api/notes/delete/<int:id>", views.notes_delete, name="notes_delete"),
    path("api/passwords/edit/<int:id>", views.passwords_edit, name="passwords_edit"),
    path("api/passwords/delete/<int:id>", views.passwords_delete, name="passwords_delete"),
    path("api/create/note", views.create_note, name="create_note"),
    path("api/create/password", views.create_password, name="create_password"),
]

