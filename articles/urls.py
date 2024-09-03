from django.urls import path
from .views import TestView


app_name = 'articles'

urlpatterns = [

	path('', TestView.as_view(), name="main")

]