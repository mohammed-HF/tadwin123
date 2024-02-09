from django.contrib import admin
from .models import CustomUser, Note

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'lastLoginDate', 'registrationDate', 'is_active', 'is_staff')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'creationDate', 'version')
