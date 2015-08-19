from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from newsFeed.views import home_page, create_page, feed_page
from newsFeed.models import Item

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)

class CreatePageTest(TestCase):

	def test_create_page_url_resolves_to_create_page(self):
		found = resolve('/newsFeed/create')
		self.assertEqual(found.func, create_page)

	def test_create_page_returns_correct_html(self):
		request = HttpRequest()
		response = create_page(request)
		expected_html = render_to_string('create.html')
		self.assertEqual(response.content.decode(), expected_html)

	def test_create_page_can_save_a_post_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['name_text'] = 'Matt'
		request.POST['phone_text'] = '808'
		request.POST['item_text'] = 'text'

		response = create_page(request)
		
		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.name, 'Matt')
		self.assertEqual(new_item.phone, '808')
		self.assertEqual(new_item.text, 'text')


class FeedPageTest(TestCase):

	def test_feed_page_url_resolves_to_feed_page(self):
		found = resolve('/newsFeed/feed')
		self.assertEqual(found.func, feed_page)

	def test_feed_page_returns_correct_html(self):
		request = HttpRequest()
		response = feed_page(request)
		expected_html = render_to_string('feed.html')
		self.assertEqual(response.content.decode(), expected_html)

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

