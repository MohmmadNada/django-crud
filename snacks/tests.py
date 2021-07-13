from django.http import response
from django.test import TestCase
# from django.conf.urls import url
from django.urls import reverse
from .models import Snack
# Create your tests here.
class SnackTest(TestCase):
    def test_list_page(self):
        url=reverse('home')# return url link 
        actual= self.client.get(url).status_code
        excepted=200
        self.assertEqual(actual,excepted)
    def test_home_template(self):
        url=reverse('home')
        actual= self.client.get(url)
        
        excepted='snack_list.html'
        self.assertEqual(actual.templates[0].name,excepted)
    def setUp(self):
        # self.snack
        self.snack = Snack.objects.create(
            title = 'testing test title',
            purchaser='testing test purchaser',
            description='testing test  description',
        )
    # def test_snack_list(self):
    #     response=self.client.get('home')
    #     print('=====>   ',response.items())
    def test_movie_create(self):
        response=self.client.post(reverse('create'),{})