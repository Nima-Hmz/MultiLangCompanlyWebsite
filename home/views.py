from django.shortcuts import render
from django.views import View
from products.models import Category, Product
from .models import FirstTitle, AboutUs, Services
from .template_manager import language_switcher

# Create your views here.


class IndexView(View):
	def get(self, request):
		lang = request.GET.get('lang', '')
		first_title = FirstTitle.objects.first()
		aboutus = AboutUs.objects.first()
		
		context = {

			'index_image1':first_title.image,
			'index_image2':first_title.image2,
			'about_image':aboutus.image,


		}

		context.update(language_switcher(first_title, lang, "index"))
		context.update(language_switcher(aboutus, lang, "about"))

		return render(request, 'home/index.html', context=context)
