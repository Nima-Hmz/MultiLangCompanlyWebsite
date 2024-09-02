from django.shortcuts import render
from django.views import View
from products.models import Category, Product

# Create your views here.


class IndexView(View):
	def get(self, request):
		category_star = Category.objects.filter(star=True)
		context = {

			'category_star':category_star

		}
		return render(request, 'home/index.html', context=context)
