from django.urls import path
from portfolio.views import detalhe_certificado, index, certificado

urlpatterns = [
        path('', index, name='index'),
        path('certificado/', certificado, name='certificado'),
        path('certificado/<str:linguagem>/', detalhe_certificado, name='detalhe_certificado')
]

