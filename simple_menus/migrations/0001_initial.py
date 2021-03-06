# Generated by Django 3.2.10 on 2021-12-16 12:59

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('label', models.CharField(max_length=255, verbose_name='label')),
                ('order', models.IntegerField(default=0)),
                ('icon', models.CharField(blank=True, help_text='Icon', max_length=50, null=True)),
                ('slug', models.SlugField(max_length=80, unique=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('classnames', models.CharField(blank=True, max_length=255, null=True, verbose_name='class names')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this menu belongs to. A menu will get all permissions granted to each of their groups.', related_name='_simple_menus_menuitem_groups_+', to='auth.Group', verbose_name='groups')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, help_text='Categories and Menu Item, unlike tags, they can have a hierarchy. You might have a Jazz Item, and under that have children items for Bebop and Big Band. Totally optional.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='menuitem_children', to='simple_menus.menuitem')),
            ],
            options={
                'verbose_name': 'Menu Item',
                'verbose_name_plural': 'Menu Items',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('template_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='template')),
                ('slug', models.SlugField(max_length=80, unique=True)),
                ('menu_root', mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='simple_menus.menuitem')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
    ]
