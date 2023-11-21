from django.test import TestCase
from restaurant.models import Menu


class MenuItemTest(TestCase):
    def set_up(self):
        Menu.objects.create(name='IceCream', price=80, inventory=100,menu_item_description='testing')


    def test_get_item(self):
        item = Menu.objects.create(name="IceCream", price=80, inventory=100,menu_item_description='testing')
        use_string = 'IceCream : 80'
        self.assertEqual(item.get_item(), use_string)