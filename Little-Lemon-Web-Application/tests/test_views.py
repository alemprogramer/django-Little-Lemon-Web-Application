from django.test import TestCase
from restaurant.models import Menu
from django.test import Client, TestCase
from django.urls import reverse


from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def set_up(self):
        Menu.objects.create(name='IceCream', price=80, inventory=100,menu_item_description='testing') 

    def test_create(self):
        data = {'name': 'latte', 'price': 2.99, 'inventory': 5, 
                'menu_item_description': 'tasty'}
        response = self.client.post(reverse('menu-items'), data=data)
        serializer = MenuSerializer(Menu.objects.get(name='latte'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, serializer.data)