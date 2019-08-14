from django.test import TestCase
from django.shortcuts import resolve_url as r
from open_event.evento.forms import InscritoForm
from open_event.evento.models import Inscrito


class InscricaoTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        """GET / Deve retornar 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """"Deve Usar inscricao_form.html"""
        self.assertTemplateUsed(self.response, 'inscricoes_form.html')

    def test_html(self):
        """Html deve ter as seguintes tags"""
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        """Html deve conter csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, InscritoForm)

    def test_form_fields(self):
        form = self.response.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))


class PostValido(TestCase):
    def setUp(self):
        data = dict(name='Kelwy Oliveira', cpf='12345678901',
                    email='kelwys@kelwys.com', phone='27-99839-1003')
        self.response = self.client.post(r('/inscricao/'), data)

    def test_post(self):
        """Valid POST redireciona /inscricao/1/"""
        self.assertRedirects(self.response, '/inscricao/1/')

    def test_save_inscricao(self):
        self.assertTrue(Inscrito.objects.exists())


class PostInvalido(TestCase):
    def setUp(self):
        self.response = self.client.post(r('/inscricao/'), {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'inscricoes_form.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, InscritoForm)

    def test_form_has_errors(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_inscricao(self):
        self.assertFalse(Inscrito.objects.exists())
