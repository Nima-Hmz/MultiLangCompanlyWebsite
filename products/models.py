from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from extensions.utils import jalali_converter

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام")
    en_name = models.CharField(max_length=200, verbose_name="نام انگلیسی")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="اسلاگ", allow_unicode  = True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children', verbose_name='دسته بندی مادر')
    description = RichTextField(verbose_name="توضیحات دسته بندی اختیاری", null=True, blank=True)
    en_description = RichTextField(verbose_name=("توضیحات دسته بندی انگلیسی اختیاری"), null=True, blank=True)

    class Meta:
        ordering = ('parent__id',)
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی‌ها"

    def get_absolute_url(self):
        return reverse('search:category_filter', args=[self.slug,])

    def __str__(self) -> str:
        return self.name


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="دسته‌بندی")
    name = models.CharField(max_length=200, verbose_name="نام")
    en_name = models.CharField(max_length=200, verbose_name="نام انگلیسی")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="آدرس" , allow_unicode  = True)
    image = models.ImageField(upload_to="products/%Y/%m/%d", verbose_name="عکس")
    description = RichTextField(verbose_name="توضیحات و اطلاعات")
    en_description = RichTextField(verbose_name="توضیحات و اطلاعات انگلیسی")
    available = models.BooleanField(default=True, verbose_name="وضعیت نمایش")
    pub_date = models.DateTimeField(default=timezone.now, verbose_name=("زمان انتشار"))
    created = models.DateTimeField(auto_now_add = True, verbose_name="ایجاد شده")
    updated = models.DateTimeField(auto_now=True, verbose_name="به‌روز شده")
    position = models.IntegerField(verbose_name="موقعیت در نمایش")
    more_product = models.ManyToManyField("self" , blank=True , null=True , verbose_name='محصولات مرتبط')

    class Meta:
        ordering = ("-position",)
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


    def __str__(self) -> str:
        return self.name

    
    def jpub_date(self):
        return jalali_converter(self.pub_date)
    


        

        
    
