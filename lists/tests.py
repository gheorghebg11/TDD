from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.shortcuts import render

from lists.views import home_page
from lists.models import Item, List


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)

        #expected_response = render(request, 'home.html')
        #self.assertEqual(response.content, expected_response.content)
        #expected_html = render_to_string('home.html', request=request)# {'new_item_text':'A new list item'}, request=request)
        #self.assertEqual(response.content.decode(), expected_html)
        

class ListAndItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        self.assertEqual(saved_items[0].text, 'The first (ever) list item')
        self.assertEqual(saved_items[1].text, 'Item the second')
        self.assertEqual(saved_items[0].list, list_)
        self.assertEqual(saved_items[1].list, list_)

class ListViewTest(TestCase):
    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world')
        self.assertTemplateUsed(response, 'list.html')


    def test_display_all_items(self):
        list_ = List.objects.create()
        Item.objects.create(text='itemey 1', list=list_)
        Item.objects.create(text='itemey 2', list=list_)
  
        response = self.client.get('/lists/the-only-list-in-the-world')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')


class NewListTest(TestCase):
    
    def test_save_a_POST_request(self):
        self.client.post('/lists/new', data={'item_text':'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first() #same as Item.objects.all()[0]
        self.assertEqual(new_item.text, 'A new list item')
        
    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'item_text':'A new list item'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world')
