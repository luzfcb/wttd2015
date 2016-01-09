from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """GET / deve retornar status code 200"""

        self.assertEquals(200, self.response.status_code)
        self.assertTemplateUsed(self.response, 'index.html')

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')
