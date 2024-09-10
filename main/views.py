from django.shortcuts import render
from .models import Product

def show_main(request):
    # Data produk statis
    products = [
        {
            'name': 'earphone',
            'price': 20000,
            'description': 'bekas pakai, barang masih terjaga. kualitas terbaik.',
            'quantity': 1
            
        },
        {
            'name': 'printer',
            'price': 150000,
            'description': 'printer keluaran tahun 2015, namun terawat',
            'quantity': 1
        },
        {
            'name': 'senter',
            'price': 40000,
            'description': 'senter kepala, untuk dapat melihat di malam hari',
            'quantity': 1
        }
    ]

    return render(request, "main.html", {'products': products})