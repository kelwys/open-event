from django.test import TestCase
from open_event.adm.models import Inscrito


class InscricaoModelTest(TestCase):
    def test_create(self):
        obj = Inscrito(
            name='Kelwy Oliveira',
            cpf='12345678901',
            email='kelwys@ucl.br',
            phone='27-99839-1003'
        )
        obj.save()
        self.assertTrue(Inscrito.objects.exists())