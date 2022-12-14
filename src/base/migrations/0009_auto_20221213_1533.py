# Generated by Django 3.2.16 on 2022-12-13 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20221213_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='author_bio',
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='base.author'),
        ),
    ]