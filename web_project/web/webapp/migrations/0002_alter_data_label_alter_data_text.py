# Generated by Django 4.2.3 on 2023-08-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='label',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='text',
            field=models.CharField(),
        ),
    ]