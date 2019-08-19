from django import forms
from django.core.exceptions import ValidationError
from open_event.evento.models import Inscrito
from open_event.utils.views import validate_cpf


class InscritoFormOld(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='Email', required=False)
    phone = forms.CharField(label='Telefone', required=False)


class InscritoForm(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = ['name', 'cpf', 'email', 'phone']

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

    def clean(self):
        self.cleaned_data = super().clean()

        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone.')

        return self.cleaned_data


class InscricaoLoteForm(forms.Form):
    arquivo = forms.FileField(label='Arquivo: ')

    def clean(self):
        cleaned_data = super(InscricaoLoteForm, self).clean()
        arquivo = cleaned_data.get("arquivo")

        if not arquivo:
            raise forms.ValidationError("Insira um arquivo.")