from django.contrib import admin
from django.utils.html import format_html

from .models.product.category import Category
from .models.product.supplier import Supplier
from .models.product.product import Product
from .models.product.item import Item

from .models.product.book.book import Book
from .models.product.book.author import Author
from .models.product.book.publisher import Publisher
from .models.product.book.genre import Genre

from .models.product.clothes.clothes import Clothes

from .models.product.mobile_phone.mobile_phone import MobilePhone

from .models.product.laptop.laptop import Laptop 

# CATEGORY
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description',]

admin.site.register(Category, CategoryAdmin)

# SUPPLIER
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'address']

admin.site.register(Supplier, SupplierAdmin)

# PRODUCT
class ProductAdmin(admin.ModelAdmin):
    def supplier_name(self, obj):
        return obj.supplier.name
    
    def category_name(self, obj):
        return obj.category.name

    list_display = ['id', 'name', 'supplier_name', 'category_name']

admin.site.register(Product, ProductAdmin)

# ITEM
class ItemAdmin(admin.ModelAdmin):
    def product_name(self, obj):
        return obj.product.name
    
    def image_view(self, obj):
        return format_html('<img src="{}" width="200" height="200" />'.format(obj.image.url))

    list_display = ['image_view', 'product_name', 'price', 'discount']

admin.site.register(Item, ItemAdmin)

# BOOK
class BookAdmin(admin.ModelAdmin):
    def book_name(self, obj):
        return obj.product.name 

    list_display = ['book_name', 'language', 'summary']
    search_fields = ['language',]
    filter_horizontal = ['authors', 'genres']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'biography']

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'email'] 

class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'age_range', 'description'] 

admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)

# CLOTHES
class ClothesAdmin(admin.ModelAdmin):
    def clothes_name(self, obj):
        return obj.product.name
    list_display = ['clothes_name', 'color', 'age', 'gender', 'material']

admin.site.register(Clothes, ClothesAdmin)

# LAPTOP
class LaptopAdmin(admin.ModelAdmin):
    def laptop_name(self, obj):
        return obj.product.name
    list_display = ['laptop_name', 'rom', 'ram', 'screen',]

admin.site.register(Laptop, LaptopAdmin)

# MOBILE PHONE
class MobilePhoneAdmin(admin.ModelAdmin):
    def mobile_phone_name(self, obj):
        return obj.product.name
    list_display = ['mobile_phone_name', 'rom', 'ram', 'screen',]

admin.site.register(MobilePhone, MobilePhoneAdmin)