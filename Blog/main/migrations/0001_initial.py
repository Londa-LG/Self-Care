# Generated by Django 3.1.1 on 2020-09-04 17:08

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('post_description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='')),
                ('post', ckeditor.fields.RichTextField()),
                ('date_created', models.DateField()),
                ('comment_count', models.IntegerField()),
                ('view_count', models.IntegerField(default=0)),
                ('featured', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(to='main.Categories')),
                ('next', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_post', to='main.post')),
                ('previous', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_post', to='main.post')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commenter', models.CharField(max_length=30)),
                ('comment', models.TextField()),
                ('date_commented', models.DateField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.post')),
            ],
        ),
    ]
