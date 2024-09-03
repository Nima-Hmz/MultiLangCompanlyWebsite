from django.shortcuts import render
from django.views import View
from .models import Article

# Create your views here.


class TestView(View):
	def get(self, request):
		return render(request, 'articles/1.html')