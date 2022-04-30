from django.shortcuts import render
from django.contrib import messages
from . import forms
from . import models


def index(request):
    context = {
        'produtos': models.Produto.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    form = forms.ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'E-mail enviado com sucesso!')
            form = forms.ContatoForm()

        else:
            messages.error(request, 'Erro ao enviar e-mail')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    if str(request.method) == 'POST':
        form = forms.ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto salvo com sucesso!')
            form = forms.ProdutoModelForm()
        else:
            messages.error(request, 'Erro ao salvar produto.')
    else:
        form = forms.ProdutoModelForm()

    context = {
        'form': form
    }

    return render(request, 'produto.html', context)
