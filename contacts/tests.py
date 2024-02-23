from django.test import TestCase


class URLTests(TestCase):    
    def test_contactshomepage(self):        
        response = self.client.get('/contacts/')        
        self.assertEqual(response.status_code, 200)