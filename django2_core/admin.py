from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Produto)
class Produto_admin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'slug', 'criado', 'editado', 'ativo')
