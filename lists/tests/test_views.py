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


class ListViewTest(TestCase):
    def test_uses_list_template(self):
        list_ = List.objects.create()
        response = self.client.get('/lists/%d/' %(list_.id) )
        self.assertTemplateUsed(response, 'list.html')


    def test_display_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text='itemey 1', list=correct_list)
        Item.objects.create(text='itemey 2', list=correct_list)
        
        other_list = List.objects.create()
        Item.objects.create(text='other list item 1', list=other_list)
        Item.objects.create(text='other list item 2', list=other_list)
  
        response = self.client.get('/lists/%d/' %(correct_list.id))

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'other list item 1')
        self.assertNotContains(response, 'other list item 2')

    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get('/lists/%d/' %(correct_list.id))

        

class NewListTest(TestCase):
    
    def test_save_a_POST_request(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post('/lists/%d/add_item' %(correct_list.id), data={'item_text':'A new item for an existing list'})
        self.assertEqual(Item.objects.count(), 1)

        new_item = Item.objects.first() #same as Item.objects.all()[0]
        self.assertEqual(new_item.text, 'A new item for an existing list')
        self.assertEqual(new_item.list, correct_list)
        
    def test_redirects_after_POST(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post('/lists/%d/add_item' %(correct_list.id), data={'item_text':'A new item for an existing list'})

        self.assertRedirects(response, '/lists/%d/' %(correct_list.id))
