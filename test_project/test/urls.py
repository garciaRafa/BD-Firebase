from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('criar_usuario/', views.criar_usuario, name='criar_usuario'),
    path('consultar_usuarios/', views.consultar_usuarios_por_idade, name='consultar_usuarios'),
    path('resultados_usuarios/', views.resultados_usuarios, name='resultados_usuarios'),
    path('sucesso/', views.sucesso, name='sucesso')
]
