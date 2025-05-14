from django.shortcuts import get_object_or_404, render

from portfolio.models import Programacao


def index(request):
        return render(request, 'portfolio/index.html')

def certificado(request):       
        #programacoes = Programacao.objects.all()
        programacoes = Programacao.objects.order_by("-data").filter(publicada=True)
        return render(request, 'portfolio/certificado.html', {"cards":programacoes})

def detalhe_certificado(request, linguagem):
        linguagem = get_object_or_404(Programacao, linguagem=linguagem)
        return render(request, 'portfolio/detalhe_certificado.html', {'programacao': linguagem})