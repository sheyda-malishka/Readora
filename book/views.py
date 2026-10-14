from django.shortcuts import render , get_object_or_404
from django.views import View
from .models import Book

from .models import Book

# Create your views here.


class HomeView(View):
    def get(self,request):
        books = Book.objects.all()
        return render(request , 'book/main.html' , {'books':books})

    def post(self , request):
        return render(request , 'book/main.html' )


class PostDetailView(View):
    def get(self , request , post_id , post_slug):
        book = get_object_or_404(Book , pk = post_id , slug = post_slug)
        return render(request , 'book/detail.html' , {'book' : book })







