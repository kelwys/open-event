import csv

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from open_event.evento.forms import InscritoForm, InscricaoLoteForm
from open_event.evento.models import Inscrito, Palestrante


def home(request):
    palestrantes = Palestrante.objects.all()
    return render(request, 'index.html', {'palestrantes': palestrantes})


def detail(request, pk):
    inscrito = Inscrito.objects.get(pk=pk)
    return render(request, 'inscricao_detail.html', {'inscrito': inscrito})


def inscricao_individual(request):
    if request.method == 'POST':
        form = InscritoForm(request.POST)

        if form.is_valid():
            inscrito = Inscrito.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/inscricao/{}/'.format(inscrito.pk))
        else:
            return render(request, 'inscricoes_form.html', {'form': form})
    else:
        context = {'form': InscritoForm()}
        return render(request, 'inscricoes_form.html', context)


@login_required
def inscricao_lote(request):
    if request.method == 'POST':
        form = InscricaoLoteForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES['arquivo']
            read_file = arquivo.read()
            arquivo_str = read_file.decode("utf-8")
            arquivo_str = arquivo_str.split('\n')

            cria_inscricao_em_lote(arquivo_str)
            x = 'msg'
            context = {'form': InscricaoLoteForm(), 'x': x}
            return render(request, 'inscricao_lote.html', context)
        else:
            return render(request, 'index.html')
    else:
        context = {'form': InscricaoLoteForm()}
        return render(request, 'inscricao_lote.html', context)


def cria_inscricao_em_lote(arquivo_str):
    reader = csv.DictReader(arquivo_str, delimiter=',')

    for row in reader:
        Inscrito.objects.get_or_create(name=row['name'], cpf=row['cpf'], email=row['email'], phone=row['phone'])
