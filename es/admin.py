from django.contrib import admin
from .models import email_model
# Register your models here.
from tinymce.widgets import TinyMCE
from django.db import models


class email_Admin(admin.ModelAdmin):



    formfield_overrides={
        models.TextField:{'widget':TinyMCE()}
    }
admin.site.register(email_model,email_Admin)