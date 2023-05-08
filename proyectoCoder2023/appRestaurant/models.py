from django.db import models
from django.db.models import UniqueConstraint, Deferrable

class tablCategoria (models.Model):
    campNombre = models.CharField(max_length=100, help_text="Ingrese un nombre para la categoria.")
    campDescrip = models.CharField(max_length=300, help_text="Ingrese una descripcion para la categoria.", null=True)
    campActivo = models.CharField(max_length=2, help_text="Ingrese si la categoria es activa o no.", default="SI")
    
    UniqueConstraint(name="restr_campNombre", fields="campNombre")
    
    def __str__(self):
        return self.campNombre + "," + self.campDescrip + "," + self.campActivo
    
    
class tablSucursal(models.Model):
    campSucNombre = models.CharField(max_length=100, help_text="Ingrese un nombre para la sucursal")
    campSucDireccion = models.CharField(max_length=300, help_text="Ingrese una dirección para la sucursal.", null=True)
    campSucLocalidad = models.CharField(max_length=30, help_text="Ingrese una localidad para la sucrusal.", null=True)
    campSucEmail = models.EmailField(help_text="Ingrese un email para la sucursal.", null=True)
    campSucTelef = models.CharField(max_length = 30, help_text="Ingrese un número de telefono para la sucursal.", null=True)
    
    UniqueConstraint(name="restr_campSucNombre", fields="campSucNombre")
    
    def __str__(self):
        return self.campSucNombre + "," + self.campSucDireccion + "," + self.campSucLocalidad + "," + self.campSucEmail + "," + self.campSucTelef
    
class tablCamarero(models.Model):
    campCamApellidoNombre = models.CharField(max_length=150, help_text="Ingrese un apellido y nombre para el camarero.")
    campCamSucursal = models.ForeignKey(tablSucursal, on_delete=models.PROTECT, help_text="Seleccione la sucursal donde esta el camarero.")
    campFecNacim = models.DateTimeField(help_text="Ingrese la fecha de nacimiento del camarero.")
    campCamActivo = models.CharField(max_length=2, help_text="Seleccione si el camarero esta activo.", default="SI")
    
    UniqueConstraint(name="restr_campCamNombre", fields="campCamApellidoNombre")
    
    def __str__(self):
        return self.campCamApellidoNombre + "," + self.campCamSucursal + "," + self.campFecNacim + "," + self.campCamActivo
    
class tablMesa(models.Model):
    campMesSigla = models.CharField(max_length=15, help_text="Ingrese una sigla para identificar la mesa.")
    campMesSuc = models.ForeignKey(tablSucursal, on_delete=models.PROTECT, help_text="Seleccione la sucursal a cual pertenece la mesa.")
    campMesActivo = models.CharField(max_length=2, help_text="Seleccione si la mesa esta activa.", default="SI")
    
    UniqueConstraint(name="restr_campMesSigla", fields="campMesSigla")
    
    def __str__(self):
        return self.campMesSigla + "," + self.campMesSuc + "," + self.campMesActivo
    
class tablItems(models.Model):
    campCartNombre = models.CharField(max_length=100, help_text="Ingrese un nombre para el item del menu.")
    campCartDescrip = models.CharField(max_length=300, help_text="Ingrese una descripcion para el item del menu.")
    campCategoria = models.ForeignKey(tablCategoria, on_delete=models.PROTECT, help_text="Ingrese una categoria para el item del menu.")
    campPrecio = models.DecimalField(max_digits=10, decimal_places=2, help_text="Ingrese un precio para el item del menu.")

    def __str__(self):
        return self.campCartNombre + "," + self.campCartDescrip + "," + self.campCategoria + "," + self.campPrecio
    
class tablOrden(models.Model):
    campOrdItem = models.ForeignKey(tablItems, on_delete=models.PROTECT, help_text="Seleccione el item de la orden.")
    campOrdFecEmis = models.DateField()
    campOrdCamarero = models.ForeignKey(tablCamarero, on_delete=models.PROTECT, help_text="Ingrese el camarero que realiza el pedido.")
    campOrdEstado = models.CharField(max_length=10, help_text="Ingrese el estado de la orden.")
    
    def __str__(self):
        return self.campOrdItem + "," + self.campOrdFecEmis + "," + self.campOrdCamarero + "," + self.campOrdEstado
