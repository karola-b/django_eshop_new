from django.shortcuts import render
from django.views.generic import ListView
from mainapp.models import Product


class ProductListView(ListView):
    model = Product
