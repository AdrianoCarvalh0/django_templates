import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    nome_da_empresa = "Ifsuldeminas"
    descricao_da_empresa = "Em 2008, o Governo Federal deu um salto na educação do país com a criação dos Institutos Federais. " \
                           "Por meio da Rede Federal de Educação Profissional, Científica e Tecnológica, 31 centros federais de " \
                           "educação tecnológica (Cefets), 75 unidades descentralizadas de ensino (Uneds), 39 escolas agrotécnicas," \
                           " 7 escolas técnicas federais e 8 escolas vinculadas a universidades " \
                           "deixaram de existir para formarem os Institutos Federais de Educação, Ciência e Tecnologia."
    contato = {
        "endereco": "Rua tiradentes,416",
        "telefone": "3464-1200",
        "email": "contato@ifsuldemina.edu.br"

    }
    cursos = {
        "1": {"titulo":"Django Fundamentos","descricao":"Fundamentos do Django"},
        "2": {"titulo":"Django Templates","descricao":"Fundamentos dos Templates"},
        "3": {"titulo":"Django ORM","descricao":"Aprenda a mexer com banco de dados"}
    }
    agora =  datetime.datetime.now()

    return render(request, 'index.html',{'nome_da_empresa':nome_da_empresa, 'descricao_da_empresa':descricao_da_empresa, 'contato':contato,'cursos':cursos,'agora':agora})


def sobre(request):
    return HttpResponse("Página sobre")

def contato(request):
    return HttpResponse("Página contato")
