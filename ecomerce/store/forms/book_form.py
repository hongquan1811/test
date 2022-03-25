from django import forms
from ..models.product.book.author import Author
from ..models.product.book.genre import Genre
from ..models.product.book.publisher import Publisher
from ..models.product.book.book import Book

class BookForm(forms.ModelForm):
    
    LANGUAGES = [
        ('en', 'English'),
        ('vi', 'Vietnamese'),
        ('kr', 'Korean'),
        ('cn', 'Chinese')
    ]

    language = forms.ChoiceField(
        choices=LANGUAGES,
    )
    number_of_pages = forms.IntegerField()
    summary = forms.CharField(widget=forms.Textarea)
    isbn = forms.CharField(max_length=20)

    publisher = forms.ModelChoiceField(queryset=Publisher.objects.all())
    genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), widget=forms.CheckboxSelectMultiple)
    author = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Book
        fields = ['language', 'number_of_pages', 'summary', 'isbn', 'publisher', 'genre', 'author']
    