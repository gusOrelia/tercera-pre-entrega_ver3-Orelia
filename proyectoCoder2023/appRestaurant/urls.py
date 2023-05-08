from django.urls import path
from appRestaurant import views

urlpatterns = [
   
    path('', views.llamInicio, name="Inicio"), #Pagina inicio de la aplicacion.
    path('listadoCategoria',views.llamCategoria,name='listadoCategoria'),
    path('formNuevaCateg',views.llamFormNuevaCategoria,name='formNuevaCateg'),
    path('llamFormModifCategoria/<int:pk>/',views.llamFormModifCategoria,name="categoria_modificar"),
    path('buscarCateg',views.llamBusquedaCategoria, name='buscarCateg'),
    path('buscar',views.llamABuscarCateg, name='buscar'),
]