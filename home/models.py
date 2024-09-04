from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class FirstTitle(models.Model):
	title = models.CharField(verbose_name='عنوان', max_length=200)
	entitle = models.CharField(verbose_name='عنوان انگلیسی', max_length=200)
	description = HTMLField(verbose_name='توضیحات')
	endescription = HTMLField(verbose_name='توضیحات انگلیسی')
	image = models.ImageField(upload_to='first_title/', verbose_name=("تصویر"))
	location = models.TextField(verbose_name='موقعیت مکانی')

	def __str__(self):
		return self.title

	def get_title(self, lang=''):
		return getattr(self, f'{lang}title', self.title)

	def get_description(self, lang=''):
		return getattr(self, f'{lang}description', self.description)

	class Meta:
		verbose_name = ("صفحه اصلی")
		verbose_name_plural = ("صفحه اصلی")


class AboutUs(models.Model):
	title = models.CharField(verbose_name='عنوان', max_length=200)
	entitle = models.CharField(verbose_name='عنوان انگلیسی', max_length=200)
	description = HTMLField(verbose_name='توضیحات')
	endescription = HTMLField(verbose_name='توضیحات انگلیسی')
	image = models.ImageField(upload_to='about_us/', verbose_name=("تصویر"))

	def __str__(self):
		return self.title

	def get_title(self, lang=''):
		return getattr(self, f'{lang}title', self.title)

	def get_description(self, lang=''):
		return getattr(self, f'{lang}description', self.description)

	class Meta:
		verbose_name = ("درباره ما")
		verbose_name_plural = ('درباره ما')


class ContactUs(models.Model):
	title = models.CharField(verbose_name='عنوان', max_length=200)
	entitle = models.CharField(verbose_name='عنوان انگلیسی', max_length=200)
	phone_number = models.CharField(max_length=200, verbose_name='شماره تماس')
	email = models.EmailField(verbose_name='ایمیل')
	address = models.TextField(verbose_name='آدرس')
	enaddress = models.TextField(verbose_name='آدرس انگلایسی')


	def __str__(self):
		return self.title

	def get_title(self, lang=''):
		return getattr(self, f'{lang}title', self.title)

	def get_address(self, lang=''):
		return getattr(self, f'{lang}address', self.address)

	class Meta:
		verbose_name = ("تماس با ما")
		verbose_name_plural = ('تماس با ما')



class Services(models.Model):
	title = models.CharField(verbose_name='عنوان', max_length=200)
	entitle = models.CharField(verbose_name='عنوان انگلیسی', max_length=200)

	image1 = models.ImageField(upload_to='services/', verbose_name=("تصویر1 از سمت چپ"))
	description1 = models.CharField(verbose_name='توضیحات عکس ۱', max_length=200)
	endescription1 = models.CharField(verbose_name='توضیحات عکس ۱ انگلیسی', max_length=200)

	image2 = models.ImageField(upload_to='services/', verbose_name=("تصویر2 از سمت چپ"))
	description2 = models.CharField(verbose_name='توضیحات عکس 2', max_length=200)
	endescription2 = models.CharField(verbose_name='توضیحات عکس 2 انگلیسی', max_length=200)

	image3 = models.ImageField(upload_to='services/', verbose_name=("تصویر3 از سمت چپ"))
	description3 = models.CharField(verbose_name='توضیحات عکس 3', max_length=200)
	endescription3 = models.CharField(verbose_name='توضیحات عکس 3 انگلیسی', max_length=200)

	image4 = models.ImageField(upload_to='services/', verbose_name=("تصویر4 از سمت چپ"))
	description4 = models.CharField(verbose_name='توضیحات عکس 4', max_length=200)
	endescription4 = models.CharField(verbose_name='توضیحات عکس 4 انگلیسی', max_length=200)

	image5 = models.ImageField(upload_to='services/', verbose_name=("تصویر5 از سمت چپ"))
	description5 = models.CharField(verbose_name='توضیحات عکس 5', max_length=200)
	endescription5 = models.CharField(verbose_name='توضیحات عکس 5 انگلیسی', max_length=200)


	def __str__(self):
		return self.title

	def get_title(self, lang=''):
		return getattr(self, f'{lang}title', self.title)

	def get_description(self, lang='', number=1):
		return getattr(self, f'{lang}description{number}')

	class Meta:
		verbose_name = ("خدمات")
		verbose_name_plural = ('خدمات')