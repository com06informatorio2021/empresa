# Generated by Django 4.0 on 2021-12-08 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bienvenido', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='apodo',
            field=models.CharField(default='sin apodo', max_length=100),
        ),
    ]
