# Generated by Django 4.2.2 on 2023-06-09 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Sales',
        ),
    ]
