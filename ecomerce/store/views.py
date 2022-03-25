from unicodedata import category
from urllib import request

from .models.product.book.book import Book
from .models.product.product import Product
from .models.product.category import Category
from .models.product.item import Item

from .serializers.product.product_serializer import ProductSerializer
from .serializers.product.item_serializer import ItemSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from .forms.product_form import ProductForm
from .forms.book_form import BookForm
from .forms.laptop_form import LaptopForm
from .forms.mobile_phone_form import MobilePhoneForm
from .forms.item_form import ItemForm
import io


    
def dashboard(request):
    return render(request, 'store/dashboard.html')


# Create your views here.
def index(request):
    products = Product.objects.all()
    products_serializer = ProductSerializer(products, many=True)
    products_jsonRender = JSONRenderer().render(products_serializer.data)
    stream = io.BytesIO(products_jsonRender)
    products_jsonParser = JSONParser().parse(stream)
    print(products_jsonParser)

    context = {
        'books': [p for p in products_jsonParser if p['category']['id'] == 1],
        'laptops': [p for p in products_jsonParser if p['category']['id'] == 2],
        'moblie_phones': [p for p in products_jsonParser if p['category']['id'] == 3],
        # 'clothes': [p for p in products_jsonParser if p['category']['id'] == 4],
    }

    return render(request, 'store/products.html', context)

def getItems(request):
    items = Item.objects.all()
    items_serializer = ItemSerializer(items, many=True)
    items_jsonRender = JSONRenderer().render(items_serializer.data)
    stream = io.BytesIO(items_jsonRender)
    items_jsonParser = JSONParser().parse(stream)

    context = {
        'books': [i for i in items_jsonParser if i['product']['category']['id'] == 1],
        'laptops': [i for i in items_jsonParser if i['product']['category']['id'] == 2],
        'moblie_phones': [i for i in items_jsonParser if i['product']['category']['id'] == 3],
        # 'clothes': [i for i in items_jsonParser if i['product']['category']['id'] == 4],
    }

    return render(request, 'store/items.html', context)

def addBook(request):
    if (request.method=="POST"):
        product_form = ProductForm(request.POST)
        book_form = BookForm(request.POST)
        if product_form.is_valid() and book_form.is_valid():

            product = product_form.save(commit = False)
            category = Category.objects.get(pk=1)
            product.category = category
            product.save()

            book = book_form.save(commit = False)
            book.product = product 
            book.save()

            return render(request, 'store/listBook.html')
    else:
        product_form = ProductForm()
        book_form = BookForm()
        return render(request, 'store/add_book.html',
            {
                'product_form': product_form,
                'book_form': book_form
            }
        )

def updateBook(request, product_id):
    book = Book.objects.get(pk=product_id)
    product = Product.objects.get(pk=product_id)
    bookForm = BookForm(instance=book)
    productForm = ProductForm(instance=product)
    if (request.method=="POST"):
        bookForm =BookForm(request.POST, instance=book)
        productForm = ProductForm(request.POST, instance=product)
        if(bookForm.is_valid() and productForm.is_valid() ):
            bookForm.save()
            productForm.save()
            return redirect("/")
    context = {
        'bookForm' :bookForm,
        'productForm' : productForm
        }
    return render(request, 'store/update_book.html', context )

def addLaptop(request):
    if (request.method=="POST"):
        product_form = ProductForm(request.POST)
        laptop_form = LaptopForm(request.POST)
        if product_form.is_valid() and laptop_form.is_valid():

            product = product_form.save(commit = False)
            category = Category.objects.get(pk=2)
            product.category = category
            product.save()

            laptop = laptop_form.save(commit = False)
            laptop.product = product 
            laptop.save()

            return redirect('/')
    else:
        product_form = ProductForm()
        laptop_form = LaptopForm()
        return render(request, 'store/add_laptop.html',
            {
                'product_form': product_form,
                'laptop_form': laptop_form,
            }
        )
    
    
def addMobilePhone(request):
    if (request.method=="POST"):
        product_form = ProductForm(request.POST)
        mobile_phone_form = MobilePhoneForm(request.POST)
        if product_form.is_valid() and mobile_phone_form.is_valid():

            product = product_form.save(commit = False)
            category = Category.objects.get(pk=3)
            product.category = category
            product.save()

            mobile_phone = mobile_phone_form.save(commit = False)
            mobile_phone.product = product 
            mobile_phone.save()

            return redirect('/')
    else:
        product_form = ProductForm()
        mobile_phone_form = MobilePhoneForm()
        return render(request, 'store/add_mobile_phone.html',
            {
                'product_form': product_form,
                'mobile_phone_form': mobile_phone_form,
            }
        )
    
def addItem(request, product_id):
    if (request.method=="POST"):
        item_form = ItemForm(request.POST)
        if item_form.is_valid():
            print("hi")
            print(product_id)
    else:
        item_form = ItemForm()
        return render(request, 'store/add_item.html',
            {
                'product_id': product_id,
                'item_form': item_form,
            }
        )


