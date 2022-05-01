from django.urls import path
from . import views

app_name = 'django2_core'
urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('produto/', views.produto, name='produto'),
    path('cadastrar/', views.cadastrar, name='cadastrar')
]
