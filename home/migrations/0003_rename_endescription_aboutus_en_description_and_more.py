# Generated by Django 5.0 on 2024-09-04 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_services_image1_alter_services_image2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutus',
            old_name='endescription',
            new_name='en_description',
        ),
        migrations.RenameField(
            model_name='aboutus',
            old_name='entitle',
            new_name='en_title',
        ),
        migrations.RenameField(
            model_name='aboutus',
            old_name='description',
            new_name='fa_description',
        ),
        migrations.RenameField(
            model_name='aboutus',
            old_name='title',
            new_name='fa_title',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='enaddress',
            new_name='en_address',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='entitle',
            new_name='en_title',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='address',
            new_name='fa_address',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='title',
            new_name='fa_title',
        ),
        migrations.RenameField(
            model_name='firsttitle',
            old_name='endescription',
            new_name='en_description',
        ),
        migrations.RenameField(
            model_name='firsttitle',
            old_name='entitle',
            new_name='en_title',
        ),
        migrations.RenameField(
            model_name='firsttitle',
            old_name='description',
            new_name='fa_description',
        ),
        migrations.RenameField(
            model_name='firsttitle',
            old_name='title',
            new_name='fa_title',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='endescription1',
            new_name='en_description1',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='endescription2',
            new_name='en_description2',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='endescription3',
            new_name='en_description3',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='endescription4',
            new_name='en_description4',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='endescription5',
            new_name='en_description5',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='entitle',
            new_name='en_title',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='description1',
            new_name='fa_description1',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='description2',
            new_name='fa_description2',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='description3',
            new_name='fa_description3',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='description4',
            new_name='fa_description4',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='description5',
            new_name='fa_description5',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='title',
            new_name='fa_title',
        ),
    ]
