from enum import Enum

from django.db import models
from open_event.utils.views import validate_cpf


class Inscrito(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf])
    email = models.EmailField('e-mail')
    phone = models.CharField('Telefone', max_length=20)
    date = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscrição'
        ordering = ('-date',)

    def __str__(self):
        return self.name


class NivelPatrocinio(Enum):
    SILVER = 1
    GOLD = 2


NIVEL_PATROCINIO = ((NivelPatrocinio.SILVER.value, 'Silver'),
                    (NivelPatrocinio.GOLD.value, 'Gold'))


class Patrocinio(models.Model):
    name = models.CharField('nome', max_length=100)
    photo = models.URLField('foto')
    nivel = models.IntegerField('Nivel', choices=NIVEL_PATROCINIO)

    class Meta:
        verbose_name_plural = 'Patrocinios'
        verbose_name = 'Patrocinio'

    def __str__(self):
        return self.name


class Palestrante(models.Model):
    name = models.CharField('nome', max_length=255)
    social_midia = models.CharField('social midia', max_length=20, blank=True)
    photo = models.URLField('foto')
    website = models.URLField('website', blank=True)
    description = models.TextField('descrição', blank=True)

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

    def __str__(self):
        return self.name


class Agenda(models.Model):
    palestrante = models.ForeignKey('Palestrante', on_delete=models.PROTECT)
    nome_palestra = models.CharField('Nome da Palestra', max_length=50)
    date = models.DateField('Data')
    time = models.TimeField('Hora')

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'

    def __str__(self):
        return self.nome_palestra
