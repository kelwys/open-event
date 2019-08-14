from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from open_event.evento.forms import InscritoForm
from open_event.evento.models import Inscrito, Palestrante


def home(request):
    palestrantes = Palestrante.objects.all()
    return render(request, 'index.html', {'palestrantes': palestrantes})


def detail(request, pk):
    inscrito = Inscrito.objects.get(pk=pk)
    return render(request, 'inscricao_detail.html', {'inscrito': inscrito})


def inscricao(request):
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
