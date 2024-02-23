from django.test import TestCase


class URLTests(TestCase):    
    def test_statusshomepage(self):        
        response = self.client.get('/status/')        
        self.assertEqual(response.status_code, 200)