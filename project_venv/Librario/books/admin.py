from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.books_model)
admin.site.register(models.borrow_model)
admin.site.register(models.comment_model)


