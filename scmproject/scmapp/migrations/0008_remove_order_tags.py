# Generated by Django 4.1.7 on 2023-03-30 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scmapp', '0007_alter_order_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
    ]
