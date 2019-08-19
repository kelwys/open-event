
from django.test import TestCase
from open_event.evento.models import Inscrito


class InscricaoModelTest(TestCase):
    def setUp(self):
        self.obj = Inscrito(
            name='Kelwy Oliveira',
            cpf='12345678901',
            email='kelwys@ucl.br',
            phone='27-99839-1003'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Inscrito.objects.exists())

    def test_str(self):
        self.assertEqual('Kelwy Oliveira', str(self.obj))

