# Generated by Django 3.2.9 on 2021-12-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_price',
            field=models.IntegerField(),
        ),
    ]
