# Generated by Django 3.1.1 on 2020-09-04 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='commenter',
            new_name='Name',
        ),
    ]
