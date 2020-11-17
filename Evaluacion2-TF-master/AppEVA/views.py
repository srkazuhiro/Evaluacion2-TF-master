from django.shortcuts import render
from . import models
from .forms import CustomUserForm


# Create your views here.

def AppEVA(request):
    imagenes=models.Foto.objects.all()
    datos={"fotos":imagenes}
    return render(request, 'index.html', datos)



def registro_usuario(request):
    
    return render(request, 'registration/registrar.html')