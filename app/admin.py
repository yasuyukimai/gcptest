# Register your models here.
from django.contrib import admin
from .models import Model  # YourModel は自分のモデルの名前に置き換えてください

admin.site.register(Model)