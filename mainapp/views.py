from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from mainapp.models import Product


class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = "__all__"
    success_url = reverse_lazy('list_view')
