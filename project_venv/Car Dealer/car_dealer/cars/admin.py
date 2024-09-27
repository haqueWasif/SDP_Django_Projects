from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.car_model)
admin.site.register(models.car_comment)
admin.site.register(models.car_purchase)


