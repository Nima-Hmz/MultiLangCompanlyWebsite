# Generated by Django 5.0 on 2024-09-02 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_remove_category_created_remove_category_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(help_text='تصویری که میخواهید به عنوان کاور مقاله قرار بگیرد را وارد کنید', upload_to='articles/', verbose_name='تصویر مقاله'),
        ),
    ]
