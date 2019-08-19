from django.test import TestCase


class InscricaoLoteTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/admin/inscricao_lote/')

    def test_get(self):
        """Deve retornar status 302"""
        self.assertEqual(302, self.response.status_code)

