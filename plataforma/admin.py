from django.contrib import admin

# Register your models here.
from .models import Clientes, DadosCliente

admin.site.register(Clientes)
admin.site.register(DadosCliente)
# admin.site.register(Refeicao)
# admin.site.register(Opcao)