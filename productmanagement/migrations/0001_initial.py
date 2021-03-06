# Generated by Django 3.1.1 on 2021-03-31 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='BOOK TITLE', max_length=200)),
                ('author', models.CharField(default='AUTHOR', max_length=200)),
                ('image', models.ImageField(default='', null=True, upload_to='product/images')),
                ('price', models.IntegerField()),
                ('publisher', models.CharField(max_length=200)),
                ('edition', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('language', models.CharField(default='', max_length=200)),
                ('pages', models.CharField(default='', max_length=2000)),
            ],
        ),
    ]
