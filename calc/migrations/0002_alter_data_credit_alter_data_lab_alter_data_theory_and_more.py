# Generated by Django 4.0.4 on 2022-07-03 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='credit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='lab',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='theory',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='tutorial',
            field=models.IntegerField(),
        ),
    ]
