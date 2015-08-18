from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
	return render(request, 'home.html')

def create_page(request):
	if request.method == 'POST':
		return HttpResponse(request.POST['name_text', 'phone_text', 'item_text'])
	return render(request, 'create.html')

def feed_page(request):
	return render(request, 'feed.html', {
		'name': request.POST.get('name_text', ''), 
		'phone': request.POST.get('phone_text', ''), 
		'text': request.POST.get('item_text', '')
		})
