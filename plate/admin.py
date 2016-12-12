from django.contrib import admin

# Register your models here.
from .models import Fixture, Selection

admin.site.register(Fixture)
admin.site.register(Selection)
