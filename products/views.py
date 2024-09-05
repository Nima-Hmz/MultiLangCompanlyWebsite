from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Product, Category
from home.template_manager import language_switcher

# Create your views here.



class ProductsView(View):
	def get(self, request):
		lang = request.GET.get('lang', 'fa')
		valid_langs = ['en', 'fa']
		if lang not in valid_langs:
			lang = 'fa'

		root_categories = Category.objects.filter(parent__isnull=True)
		context = {

			'root_categories':root_categories,

		}
			
		return render(request, 'products/products.html', context)


class ProductListView(View):
	def get(self, request, slug):
		category = get_object_or_404(Category, slug=slug)
		products = category.products.all()
		context = {

			'products':products,

		}
		return render(request, 'products/product_list.html', context)
