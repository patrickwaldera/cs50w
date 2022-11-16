from datetime import datetime
import json
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, "mypasswords/home.html")
    else:
        return render(request, "mypasswords/index.html")


def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "mypasswords/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "mypasswords/login.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "mypasswords/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "mypasswords/register.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


@login_required(login_url='login')
def home(request):
    return render(request, "mypasswords/home.html")


@login_required(login_url='login')
def passwords(request):
    return render(request, "mypasswords/passwords.html")


@login_required(login_url='login')
def notes(request):
    return render(request, "mypasswords/notes.html")


@login_required(login_url='login')
def generator(request):
    return render(request, "mypasswords/generator.html")


@login_required(login_url='login')
def new(request):
    return render(request, "mypasswords/new.html")


@login_required(login_url='login')
def notes_api(request):

    notes = Notes.objects.filter(
            owner_note=request.user
        )

    notes = notes.order_by("-timestamp").all()
    return JsonResponse({
        "notes": [note.serialize() for note in notes]}
        , safe=False)


@login_required(login_url='login')
def passwords_api(request):

    passwords = PasswordCard.objects.filter(
            owner_password=request.user
        )

    passwords = passwords.order_by("-timestamp").all()
    return JsonResponse({
        "passwords": [password.serialize() for password in passwords]}
    , safe=False)


@login_required(login_url='login')
def allitens(request):

    notes = Notes.objects.filter(
            owner_note=request.user
        )

    notes = notes.order_by("-timestamp").all()

    passwords = PasswordCard.objects.filter(
            owner_password=request.user
        )

    passwords = passwords.order_by("-timestamp").all()

    return JsonResponse({
        "notes":[note.serialize() for note in notes],
        "passwords":[password.serialize() for password in passwords], 
    }, safe=False)

@csrf_exempt
def notes_edit(request, id):

    if request.method != "PUT":
        return JsonResponse({"error": "PUT request required."}, status=400)

    if not request.user.is_authenticated:
        return JsonResponse({"error": "Unauthorized request."}, status=401)

    try:
        note = Notes.objects.get(pk=id)
    except Notes.DoesNotExist:
        return JsonResponse({"error": "Note not found."}, status=404)

    if note.owner_note != request.user: 
        return JsonResponse({"error": "Not authorized to edit this note"}, status=403)

    data = json.loads(request.body)

    if data.get("name") is None or data.get("content") is None :
        return JsonResponse({"error": "Name and Content must be provided!"}, status=400)

    if data.get("name") == "" or data.get("content") == "":
        return JsonResponse({"error": "Name and Content can't be empty!"}, status=400)

    note.name = data["name"]
    note.note = data["content"]
    note.save()
    return JsonResponse({"message": "Note edited successfully"}, status=200)

@csrf_exempt
def notes_delete(request, id):

    if request.method != "DELETE":
        return JsonResponse({"error": "DELETE request required."}, status=400)

    if not request.user.is_authenticated:
        return JsonResponse({"error": "Unauthorized request."}, status=401)

    try:
        note = Notes.objects.get(pk=id)
    except Notes.DoesNotExist:
        return JsonResponse({"error": "Note not found."}, status=404)

    if note.owner_note != request.user: 
        return JsonResponse({"error": "Not authorized to edit this note"}, status=403)

    note.delete()
    return JsonResponse({"message": "Note deleted successfully"}, status=200)

@csrf_exempt
def passwords_edit(request, id):

    if request.method != "PUT":
        return JsonResponse({"error": "PUT request required."}, status=400)

    if not request.user.is_authenticated:
        return JsonResponse({"error": "Unauthorized request."}, status=401)

    try:
        password = PasswordCard.objects.get(pk=id)
    except PasswordCard.DoesNotExist:
        return JsonResponse({"error": "Note not found."}, status=404)

    if password.owner_password != request.user: 
        return JsonResponse({"error": "Not authorized to edit this note"}, status=403)

    data = json.loads(request.body)

    if data.get("name") is None or data.get("login") is None or data.get("password") is None or data.get("link")  is None:
        return JsonResponse({"error": "All Content must be provided!"}, status=400)

    if data.get("name") == "" or data.get("login") == "" or data.get("password") == "" or data.get("link") == "":
        return JsonResponse({"error": "All Content can't be empty!"}, status=400)
        
    password.name = data["name"]
    password.login = data["login"]
    password.password = data["password"]
    password.link = data["link"]
    password.save()
    return JsonResponse({"message": "Password edited successfully"}, status=200)

@csrf_exempt
def passwords_delete(request, id):

    if request.method != "DELETE":
        return JsonResponse({"error": "DELETE request required."}, status=400)

    if not request.user.is_authenticated:
        return JsonResponse({"error": "Unauthorized request."}, status=401)

    try:
        password = PasswordCard.objects.get(pk=id)
    except PasswordCard.DoesNotExist:
        return JsonResponse({"error": "Note not found."}, status=404)

    if password.owner_password != request.user: 
        return JsonResponse({"error": "Not authorized to edit this note"}, status=403)

    password.delete()
    return JsonResponse({"message": "Note deleted successfully"}, status=200)

@csrf_exempt
def create_note(request):
    
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    if not request.user.is_authenticated:
        return JsonResponse({"error": "Unauthorized request."}, status=401)

    data = json.loads(request.body)

    if data.get("name") is None or data.get("content") is None:
        return JsonResponse({"error": "Name and Content must be provided!"}, status=400)

    if data.get("name") == "" or data.get("content") == "":
        return JsonResponse({"error": "Name and Content can't be empty!"}, status=400)

    note = Notes(
        owner_note=request.user,
        name=data["name"],
        note=data["content"]
    )

    note.save()
    return JsonResponse({"message": "Note created successfully."}, status=201)

@csrf_exempt
def create_password(request):
    
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    if not request.user.is_authenticated:
        return JsonResponse({"error": "Unauthorized request."}, status=401)

    data = json.loads(request.body)

    if data.get("name") is None or data.get("login") is None or data.get("password") is None or data.get("link")  is None:
        return JsonResponse({"error": "All Content must be provided!"}, status=400)

    if data.get("name") == "" or data.get("login") == "" or data.get("password") == "" or data.get("link") == "":
        return JsonResponse({"error": "All Content can't be empty!"}, status=400)

    password = PasswordCard(
        owner_password=request.user,
        name = data["name"],
        login = data["login"],
        password = data["password"],
        link = data["link"]
    )
    password.save()
    return JsonResponse({"message": "Password created successfully."}, status=201)
