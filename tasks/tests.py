from django.test import TestCase


class URLTests(TestCase):    
    def test_taskshomepage(self):        
        response = self.client.get('/tasks/')        
        self.assertEqual(response.status_code, 200)