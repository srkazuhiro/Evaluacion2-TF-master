from django.contrib import admin

# Register your models here.
from .models import Categoria
from .models import Foto


admin.site.register(Categoria)
admin.site.register(Foto)
