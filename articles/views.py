from django.shortcuts import render
from django.views import View
from .models import Article

# Create your views here.


class ArticleListView(View):
	def get(self, request):
		context = {

			'article_temp':True

		}
		return render(request, 'articles/article_list.html', context)