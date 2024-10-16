from django.urls import path
from app_crm import views

urlpatterns = [
    # rota,view responsavel, nome referencia
    path('',views.home,name='home'),
    #path('devaprender/'),
    path('usuarios/',views.usuarios,name='listagem_usuarios'),
]
