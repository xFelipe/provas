
from django.shortcuts import render
from .models import Resposta
from .models import Questao

# Create your views here.


def view_prova(request):
    prova = []
    for questao in Questao.objects.all():
        questao_completa = dict()
        questao_completa['contexto'] = questao
        questao_completa['respostas'] = Resposta.objects.filter(id_questao_id = questao.id)
        prova.append(questao_completa)
    print(prova)
    return render(request, 'template_prova.html', {'prova': prova})


def resultado(request):
    acertos = 0
    erros = 0
    for key, value in request.GET.items():
        if Questao.objects.filter(id=1).first().resposta_correta.id == int(value):
            acertos += 1
        else:
            erros += 1
    return render(request, 'template_resultado.html', {'acertos': acertos, 'erros':erros})