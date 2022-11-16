from django.contrib import admin
from .models import * 

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass

class PasswordCardAdmin(admin.ModelAdmin):
    list_display = ("id", "owner_password", "name")

class NotesAdmin(admin.ModelAdmin):
    list_display = ("id", "owner_note", "name")

admin.site.register(User, UserAdmin)
admin.site.register(PasswordCard, PasswordCardAdmin)
admin.site.register(Notes, NotesAdmin)
