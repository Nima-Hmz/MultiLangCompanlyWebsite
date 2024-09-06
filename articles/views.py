from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
from .models import Article

# Create your views here.


class ArticleListView(View):
	def get(self, request):
		lang = request.GET.get('lang', 'fa')
		valid_langs = ['en', 'fa']
		if lang not in valid_langs:
			lang = 'fa'

		articles = Article.objects.filter(status=True)
		paginator = Paginator(articles, 6)
		page = request.GET.get('page')
		article_list1 = paginator.get_page(page)
		context = {

			'article_temp':True,
			'article_list1':article_list1,


		}
		return render(request, 'articles/article_list.html', context)