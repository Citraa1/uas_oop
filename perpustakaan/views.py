from django.shortcuts import render
from perpustakaan.models import Buku

def buku(request):
    books = Buku.objects.all()
    
    context = {
        'books': books,
    }
    return render(request, 'buku.html', context)

def penerbit(request):
    return render(request, 'penerbit.html')


