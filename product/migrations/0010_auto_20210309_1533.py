# Generated by Django 3.1.7 on 2021-03-09 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20210309_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Cakes', 'Cakes'), ('Cookies', 'Cookies'), ('Pastries', 'Pastries')], max_length=10, null=True),
        ),
    ]