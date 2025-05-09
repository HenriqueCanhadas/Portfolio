from django.shortcuts import render

def index(request):
        return render(request, 'portfolio/index.html')

def certificado(request):
        return render(request, 'portfolio/certificado.html')