from django.shortcuts import render
from .models import *

def processadorIniciante1(request):
    return render(request, 'perg_resp/proc_ini-1.html')

def processadorIniciante2(request):
    return render(request, 'perg_resp/proc_ini-2.html')

def processadorIniciante3(request):
    return render(request, 'perg_resp/proc_ini-3.html')

def processadorIniciantePergunta1(request):
    if request.method == 'POST':
        resposta = request.POST.get("alternativa")
        if resposta == "b":
            ProcessadorIniciante.objects.create(correto = 1, errado = 0)
        else:
            ProcessadorIniciante.objects.create(correto = 0, errado = 1)
        context = {'resposta': resposta}
        return render(request, 'perg_resp/proc_ini_resp-1.html', context)
    return render(request, 'perg_resp/proc_ini_perg-1.html')

def processadorIniciantePergunta2(request):
    if request.method == 'POST':
        resposta = request.POST.get("alternativa")
        if resposta == "d":
            ProcessadorIniciante.objects.create(correto = 1, errado = 0)
        else:
            ProcessadorIniciante.objects.create(correto = 0, errado = 1)
        context = {'resposta': resposta}
        return render(request, 'perg_resp/proc_ini_resp-2.html', context)
    return render(request, 'perg_resp/proc_ini_perg-2.html')

def processadorIniciantePergunta3(request):
    if request.method == 'POST':
        resposta = request.POST.get("alternativa")
        if resposta == "a":
            ProcessadorIniciante.objects.create(correto = 1, errado = 0)
        else:
            ProcessadorIniciante.objects.create(correto = 0, errado = 1)
        context = {'resposta': resposta}
        return render(request, 'perg_resp/proc_ini_resp-3.html', context)
    return render(request, 'perg_resp/proc_ini_perg-3.html')

def processadorIniciantePergunta4(request):
    if request.method == 'POST':
        resposta = request.POST.get("alternativa")
        if resposta == "a":
            ProcessadorIniciante.objects.create(correto = 1, errado = 0)
        else:
            ProcessadorIniciante.objects.create(correto = 0, errado = 1)
        context = {'resposta': resposta}
        return render(request, 'perg_resp/proc_ini_resp-4.html', context)
    return render(request, 'perg_resp/proc_ini_perg-4.html')

def processadorIniciantePergunta5(request):
    if request.method == 'POST':
        resposta = request.POST.get("alternativa")
        if resposta == "d":
            ProcessadorIniciante.objects.create(correto = 1, errado = 0)
        else:
            ProcessadorIniciante.objects.create(correto = 0, errado = 1)
        context = {'resposta': resposta}
        return render(request, 'perg_resp/proc_ini_resp-5.html', context)
    return render(request, 'perg_resp/proc_ini_perg-5.html')

def processadorIniciantePergunta6(request):
    if request.method == 'POST':
        resposta = request.POST.get("alternativa")
        if resposta == "b":
            ProcessadorIniciante.objects.create(correto = 1, errado = 0)
        else:
            ProcessadorIniciante.objects.create(correto = 0, errado = 1)
        context = {'resposta': resposta}
        return render(request, 'perg_resp/proc_ini_resp-6.html', context)
    return render(request, 'perg_resp/proc_ini_perg-6.html')

def processadorIniciantePergunta7(request):
    if request.method == 'POST':
        resposta = request.POST.get("alternativa")
        if resposta == "a":
            ProcessadorIniciante.objects.create(correto = 1, errado = 0)
        else:
            ProcessadorIniciante.objects.create(correto = 0, errado = 1)
        context = {'resposta': resposta}
        return render(request, 'perg_resp/proc_ini_resp-7.html', context)
    return render(request, 'perg_resp/proc_ini_perg-7.html')

def processadorIniciantePergunta8(request):
    if request.method == 'POST':
        resposta = request.POST.get("alternativa")
        if resposta == "c":
            ProcessadorIniciante.objects.create(correto = 1, errado = 0)
        else:
            ProcessadorIniciante.objects.create(correto = 0, errado = 1)
        context = {'resposta': resposta}
        return render(request, 'perg_resp/proc_ini_resp-8.html', context)
    return render(request, 'perg_resp/proc_ini_perg-8.html')

def processadorIniciantePergunta9(request):
    if request.method == 'POST':
        resposta = request.POST.get("alternativa")
        if resposta == "b":
            ProcessadorIniciante.objects.create(correto = 1, errado = 0)
        else:
            ProcessadorIniciante.objects.create(correto = 0, errado = 1)
        context = {'resposta': resposta}
        return render(request, 'perg_resp/proc_ini_resp-9.html', context)
    return render(request, 'perg_resp/proc_ini_perg-9.html')

def processadorIniciantePergunta10(request):
    if request.method == 'POST':
        resposta = request.POST.get("alternativa")
        if resposta == "d":
            ProcessadorIniciante.objects.create(correto = 1, errado = 0)
        else:
            ProcessadorIniciante.objects.create(correto = 0, errado = 1)
        context = {'resposta': resposta}
        return render(request, 'perg_resp/proc_ini_resp-10.html', context)
    return render(request, 'perg_resp/proc_ini_perg-10.html')

def resultado(request):
    respostas = ProcessadorIniciante.objects.all()
    certo = 0
    errado = 0
    passou = 0
    for r in respostas:
        if r.correto == 1:
            certo += 1
        else:
            errado += 1
    if certo >= errado:
        passou = 1
    context = {'certo': certo, 'errado': errado, 'passou': passou}
    return render(request, 'perg_resp/resultado.html', context)
