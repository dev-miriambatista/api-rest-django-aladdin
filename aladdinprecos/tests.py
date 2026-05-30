from django.test import TestCase

class PrecosEndpointTest(TestCase):
    def test_endpoint_retorna_200(self):
        response = self.client.get('/precos/')
        self.assertEqual(response.status_code, 200)


    def test_resposta_contem_campo_data(self):
        response = self.client.get('/precos/?data=01-01-2026')
        self.assertIn('data', response.json())

    def test_resposta_contem_campo_precos(self):
        response = self.client.get('/precos/?data=01-01-2026')
        self.assertIn('precos', response.json())