from django.test import TestCase
from newsFeed.models import Item


class PostModelTest(TestCase):
    def test_saving_and_retrieving_posts(self):
        first_item = Item()
        first_item.name = 'Matt'
        first_item.phone = '808'
        first_item.text = 'text'
        first_item.save()

        second_item = Item()
        second_item.name = 'Paula'
        second_item.phone = '228'
        second_item.text = 'other text'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.name, 'Matt')
        self.assertEqual(first_saved_item.phone, '808')
        self.assertEqual(first_saved_item.text, 'text')

        self.assertEqual(second_saved_item.name, 'Paula')
        self.assertEqual(second_saved_item.phone, '228')
        self.assertEqual(second_saved_item.text, 'other text')
