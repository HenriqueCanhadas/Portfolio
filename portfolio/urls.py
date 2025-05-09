from django.urls import path
from portfolio.views import index, certificado

urlpatterns = [
        path('', index, name='index'),
        path('certificado/', certificado, name='certificado'),
]