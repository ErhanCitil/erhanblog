# Generated by Django 3.2.16 on 2022-12-14 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20221213_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ManyToManyField(related_name='articles', to='base.Author'),
        ),
    ]
