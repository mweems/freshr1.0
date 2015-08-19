from django.shortcuts import render, redirect
from django.http import HttpResponse
from newsFeed.models import Item

def home_page(request):
	return render(request, 'home.html')

def create_page(request):
	if request.method == 'POST':
		itemName = request.POST.get('name_text', 'default_name')
		itemPhone = request.POST.get('phone_text', 'default_phone')
		itemText = request.POST.get('item_text', 'default_text')
		item = Item(name=itemName, phone=itemPhone, text=itemText)
		item.save()
		return redirect('/newsFeed/feed')

	return render(request, 'create.html')

def feed_page(request):
	items = Item.objects.all()
	return render(request, 'feed.html', 
		{'items': items}
	)
