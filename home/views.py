from django.shortcuts import render
from django.views import View

# Create your views here.


class TestView(View):
	def get(self, request):
		return render(request, 'home/1.html')
