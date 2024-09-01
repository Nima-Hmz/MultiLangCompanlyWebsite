from django.shortcuts import render
from django.views import View
from .models import Product

# Create your views here.



class TestView(View):
	def get(self, request):
		my_object = Product.objects.get(id=1)
		return render(request, 'products/1.html', {'object1':my_object})
