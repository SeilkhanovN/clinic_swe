from django.contrib import admin
from . import models


admin.site.register(models.Doctor)
admin.site.register(models.Patient)
