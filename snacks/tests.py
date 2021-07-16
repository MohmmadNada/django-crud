from logging import setLogRecordFactory
from django import urls
from django.db.models.query_utils import select_related_descend
from django.http import response
from django.test import TestCase
from django.contrib.auth import get_user_model  # when called, it returns auth.user model
from django.urls import reverse
from .models import Snack
# Create your tests here.
class SnackTest(TestCase):
    def setUp(self):
        # self.snack
        self.snack = Snack.objects.create(
            title = 'testing test title',
            purchaser='testing test purchaser',
            description='testing test  description'
        )
    def test_snack_representation(self):
        # test __str__ , that return title as string from model
        excepted ='testing test title'
        actual=str(self.snack)
        # test purchaser created 
        excepted2=self.snack.purchaser
        actual2='testing test purchaser'
        self.assertEqual(excepted,actual)
        self.assertEqual(excepted2,actual2)
        
    def test_list_page(self):
        # test list(home) Page
        # 1. test status code 200 
        url=reverse('home')# return url link 
        actual= self.client.get(url)
        excepted=200
        self.assertEqual(actual.status_code,excepted)
        # 2. test Contains , the title will show in the list page
        self.assertContains(actual,'testing test title')
        # 3. check the origin snakcs in page not shown .
        self.assertNotContains(actual,'apple')
        # 4. check the template , snack_list.html
        exceptedTemplate='snack_list.html'
        self.assertTemplateUsed(actual,exceptedTemplate)
    # details , updata , delete , create
    def test_detail_page(self):
        # test detail page 
        # test status_code  
        response= self.client.get(reverse('detail',args='1'))
        self.assertEqual(response.status_code,200)        
        # test template 
        self.assertContains(response,'testing test title') 
        self.assertContains(response,'testing test purchaser') 
        self.assertContains(response,'testing test  description')
        self.assertContains(response,'delete')
        self.assertContains(response,'Update')
        self.assertNotContains(response,'apple') 
        # test contains 
        self.assertTemplateUsed(response,'snack_detail.html')
    def test_create_page(self):
        # test 1. post by content , redirect , template , statuscode
        url = reverse('create')
        response=self.client.post(url,{
            'title': 'new title for test',
            'purchaser': 'new purchaser for test',
            'description': 'new description for test',
        },follow=True)
        self.assertContains(response,'new title for test')
        self.assertRedirects(response,reverse('detail',args='2'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'snack_detail.html')
    # test update page
    def test_update_page(self):
        url=reverse(('update'),args='1')
        response=self.client.post(url,{
            'title': 'new title for test after update',
            'purchaser': 'new purchaser for test after update',
            'description': 'new description for test after update',
        },follow=True)
        self.assertEqual(response.status_code,200)
        self.assertRedirects(response,reverse('detail',args='1'))
        self.assertTemplateUsed(response,'snack_detail.html')
        self.assertContains(response,'new description for test after update')
    def test_delete_page(self):
        # test  delete page 
        url=reverse('delete',args='1')
        response=self.client.post(url,follow=True)
        # test redirect
        self.assertRedirects(response,reverse('home'))
        # test if shown in the home ? 
        self.assertNotContains(response,'testing test title')
        self.assertTemplateUsed(response,'snack_list.html')