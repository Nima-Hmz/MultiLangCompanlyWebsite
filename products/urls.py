from django.urls import path
from .views import ProductsView, ProductListView

app_name = 'products'

urlpatterns = [

	path('', ProductsView.as_view(), name='products'),
	path('product_list/<slug:slug>/', ProductListView.as_view(), name='product_list'),

]