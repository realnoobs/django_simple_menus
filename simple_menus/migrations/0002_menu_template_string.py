# Generated by Django 3.2.10 on 2021-12-16 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_menus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='template_string',
            field=models.TextField(blank=True, null=True),
        ),
    ]