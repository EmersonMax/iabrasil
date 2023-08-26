from django.urls import path
from . import views

urlpatterns = [
    path('cumprimento/', views.cumprimentar, name='cumprimentar'),
    path('', views.home, name='home'),
    path('importar/', views.importar_planilha, name='importar_planilha'),
    path('search/', views.search_view, name='search_view'),
    path('ferramenta/<int:ferramenta_id>/', views.ferramenta_detail, name='ferramenta_detail'),
    path('categoria/<str:categoria>/', views.categoria_view, name='categoria_view'),
    path('all_categories/', views.all_categories_view, name='all_categories_view'),


]