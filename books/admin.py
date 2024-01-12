from django.contrib import admin
from .models import Book


# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
# order of strings (fields) is the order of columns in the admin panel
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "owner",
        "author",
        "title",
        "edition",
        "description",
        "created_at",
        "updated_at",
    )


# Register your models here.
admin.site.register(Book, BookAdmin)
