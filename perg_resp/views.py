from django.shortcuts import render
from .models import *

def processadorIniciante(request):
    if request.method == 'POST':
        perguntas = ProcessadorIniciante.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for p in perguntas:
            total+=1
            if p.resposta ==  request.POST.get(p.pergunta):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'perg_resp/result.html',context)
    else:
        perguntas = ProcessadorIniciante.objects.all()
        context = {'perguntas': perguntas}
        return render(request, 'perg_resp/processadorIniciante.html', context)
