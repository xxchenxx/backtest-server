# Generated by Django 2.1 on 2018-08-28 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_report_author_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='author_id',
            new_name='author',
        ),
    ]
