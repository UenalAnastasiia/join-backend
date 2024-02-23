from django.test import TestCase


class URLTests(TestCase):    
    def test_usershomepage(self):        
        response = self.client.get('/users/')        
        self.assertEqual(response.status_code, 200)