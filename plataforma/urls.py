from django.urls import path
from . import views

urlpatterns = [  #Lista
    path('clientes/', views.clientes, name="clientes"),
    path('dados_cliente/', views.dados_cliente_listar, name="dados_cliente_listar"),
    path('dados_cliente/<str:id>/', views.dados_cliente, name="dados_cliente"),
    # path('grafico_peso/<str:id>/', views.grafico_peso, name="grafico_peso"),
    # path('plano_alimentar_listar/', views.plano_alimentar_listar, name="plano_alimentar_listar"),
    # path('plano_alimentar/<str:id>/', views.plano_alimentar, name="plano_alimentar"),
    # path('refeicao/<str:id_paciente>/', views.refeicao, name="refeicao"),
    # path('opcao/<str:id_paciente>/', views.opcao, name="opcao"),
]