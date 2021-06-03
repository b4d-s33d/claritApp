from django.shortcuts import render
from .models import Cliente

# Create your views here.

def index(request):  

    numClientes=Cliente.objects.all().count()

    return render(request, 'index.html',
    context={'numClientes':numClientes})  