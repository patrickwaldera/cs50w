
from asyncio.windows_events import NULL
from django.contrib.auth.models import AbstractUser
from django.db import models
from django_cryptography.fields import encrypt

# Create your models here.

class User(AbstractUser):
    def serialize(self):
        return {
            "username": self.username,
            "e-mail": self.email,
        }

class PasswordCard(models.Model):
    owner_password = models.ForeignKey(User, on_delete=models.CASCADE, related_name="passwordsuser")
    name = models.CharField(max_length=100)
    login = encrypt(models.CharField(max_length=100))
    password = encrypt(models.CharField(max_length=100))
    link = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now=True)

    def serialize(self):

        return {
            "id": self.id,
            "owner_password": self.owner_password.username,
            "name": self.name,
            "login": self.login,
            "password": self.password,
            "link": self.link,
            "timestamp": self.timestamp.strftime("%I:%M %p - %b %d %Y")
        }

class Notes(models.Model):
    owner_note = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notesuser")
    name = models.CharField(max_length=100, default=NULL)
    note = encrypt(models.CharField(max_length=500))
    timestamp = models.DateTimeField(auto_now=True)

    def serialize(self):

        return {
            "id": self.id,
            "owner_note": self.owner_note.username,
            "name": self.name,
            "note": self.note,
            "timestamp": self.timestamp.strftime("%I:%M %p - %b %d %Y")
        }