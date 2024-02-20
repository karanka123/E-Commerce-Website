from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import NewItemForm

# Create your views here.

def details(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[:3]
    return render(request, 'item/detail.html', {'item': item, 'related_items': related_items})

def newItem(request):
    if request.method == 'post':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            print(request.FILES)
            return redirect('/')  # You might want to change this redirect URL to the appropriate one
    else:  # Change 'post' to 'else'
        form = NewItemForm()
    return render(request, 'item/form.html', {'form': form})  # Change 'forms' to 'form'
