# Generated by Django 3.2.3 on 2021-05-20 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='remarks',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
