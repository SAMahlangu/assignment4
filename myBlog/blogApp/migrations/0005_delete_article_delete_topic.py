# Generated by Django 4.2 on 2023-04-12 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0004_post_author_alter_post_created_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]