from django.shortcuts import render, redirect
from django.http import HttpResponse
from newsFeed.models import Item

def home_page(request):
	return render(request, 'home.html')

def create_page(request):
	if request.method == 'POST':
		itemName = request.POST.get('name_text', '')
		itemPhone = request.POST.get('phone_text', '')
		itemText = request.POST.get('item_text', '')
		image = request.FILES.get('pic', '')
		item = Item(name=itemName, phone=itemPhone, text=itemText, image=image)
		item.save()
		return redirect('/newsFeed/feed')

	return render(request, 'create.html')

def feed_page(request):
	items = Item.objects.all().order_by("-date")
	return render(request, 'feed.html', 
		{'items': items},
	)
