from django.shortcuts import render

# Create your views here.


from item.models import Category, Item

def index(request):
    item = Item.objects.filter(is_sold = False)
    category = Category.objects.all()
    return render(request, 'core/index.html', {'items': item, 'category':category})


def contact(request):
    return render(request, 'core/contact.html')