from django.shortcuts import render
from django.views import View
from .models import Article

# Create your views here.


class TestView(View):
	def get(self, request):
		my_object = Article.objects.get(id=3)
		return render(request, 'articles/1.html', {'object1':my_object})