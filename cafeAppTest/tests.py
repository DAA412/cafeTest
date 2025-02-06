from django.test import TestCase
from .models import Order

class OrderModelTest(TestCase):

    def setUp(self):
        self.order = Order.objects.create(
            table_number=1,
            items="Pizza:10.00,Burger:5.00",
            status='waiting'
        )

    def test_order_creation(self):
        self.assertEqual(self.order.table_number, 1)
        self.assertEqual(self.order.total_price, 15.00)
        self.assertEqual(self.order.status, 'waiting')

