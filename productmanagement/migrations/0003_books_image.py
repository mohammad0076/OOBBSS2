# Generated by Django 3.1.1 on 2021-03-30 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0002_auto_20210317_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='image',
            field=models.ImageField(null=True, upload_to='s/ss'),
        ),
    ]
