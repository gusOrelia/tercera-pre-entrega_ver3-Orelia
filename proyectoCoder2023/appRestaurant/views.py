from django.shortcuts import render, redirect
from django.http import HttpResponse
from appRestaurant.models import tablCategoria
from appRestaurant.forms import formCategoria
from django.views.generic.edit import UpdateView

def llamInicio(request):
    return render(request, 'appRestaurant/pagInicio.html')

def llamCategoria(request):
    vl_categorias = tablCategoria.objects.all() # Trae todas las categorias.
    vl_listaPasar = {"categoria": vl_categorias}
    return render(request, "appRestaurant/pagListaCategoria.html",vl_listaPasar)

def llamFormNuevaCategoria(request):
    
    if request.method == 'POST':
        
        print("Paso por aqui 2")
        
        vl_formulario = formCategoria(request.POST)
        
        if vl_formulario.is_valid():
            
            vl_informacion = vl_formulario.cleaned_data
            
            vl_modCategoria = tablCategoria(campNombre = vl_informacion["campNombre"],campDescrip = vl_informacion["campDescrip"],campActivo = vl_informacion["campActivo"])
            
            vl_modCategoria.save()
            
            return redirect("listadoCategoria")
        
        else:
            print("Error")
    else:
        vl_formulario = formCategoria()
        
    return render(request, 'appRestaurant/pagFormCategoria.html', {'formCategoria': vl_formulario})

def llamFormModifCategoria(request, pk):
    
    vl_modelCategoria = tablCategoria.objects.get(id=pk)
    
    if request.method == 'POST':
    
        vl_formCategoria = formCategoria(request.POST)
        
        if(vl_formCategoria.is_valid()):
            
            vl_informacion = vl_formCategoria.cleaned_data
            
            vl_modelCategoria.campNombre = vl_informacion["campNombre"]
            vl_modelCategoria.campDescrip = vl_informacion["campDescrip"]
            vl_modelCategoria.campActivo = vl_informacion["campActivo"]
    
            vl_modelCategoria.save()
            
            return redirect("listadoCategoria")
        
    vl_formCategoria = formCategoria(initial={"campNombre":vl_modelCategoria.campNombre, "campDescrip":vl_modelCategoria.campDescrip, "campActivo":vl_modelCategoria.campActivo})    
        
    return render(request, 'appRestaurant/pagFormModiCateg.html', {'formCategoria': vl_formCategoria})
            
def llamBusquedaCategoria(request):
     return render(request,'appRestaurant/pagFormBuscarCateg.html')
 
def llamABuscarCateg(request):
     
     if request.GET['categoria']:
          vl_categoria = request.GET['categoria']
          
          vl_listaPasar= tablCategoria.objects.filter(id__icontains=vl_categoria)
          
          return render(request,'appRestaurant/pagListaCategoria.html', {"categoria":vl_listaPasar})
     else:
          vl_respuesta= "No enviaste datos"

     return HttpResponse(vl_respuesta)