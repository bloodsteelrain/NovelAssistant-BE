# Generated by Django 4.2.3 on 2023-07-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='introduce',
            field=models.TextField(blank=True, default='소개글을 입력해주세요'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]