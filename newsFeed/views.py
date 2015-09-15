from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from newsFeed.models import Item


def home_page(request):
    return render(request, 'home.html')


def create_page(request):
    if request.method == 'POST':
        itemName = request.POST.get('name_text', '')
        itemPhone = request.POST.get('phone_text', '')
        itemText = request.POST.get('item_text', '')
        image = request.FILES.get('pic', '')
        item = Item.objects.create(name=itemName, phone=itemPhone, text=itemText, image=image)
        try:
            item.full_clean()
        except ValidationError:
            item.delete()
            return render(request, 'create.html', {"error": 'Cannot have blank fields.'})
        return redirect('/newsFeed/feed')

    return render(request, 'create.html')


def feed_page(request):
    items = Item.objects.all().order_by("-date")
    return render(request, 'feed.html',
                  {'items': items},
                  )
