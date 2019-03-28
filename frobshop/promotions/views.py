from django.shortcuts import render

from oscar.apps.catalogue.views import CatalogueView
class HomeView(CatalogueView):
     template_name = 'promotions/home.html'
     # template_name = 'catalogue/partials/product.html'
