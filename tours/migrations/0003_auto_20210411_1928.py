# Generated by Django 3.1.5 on 2021-04-11 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_auto_20210411_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialpack',
            name='days',
            field=models.IntegerField(default='5'),
        ),
        migrations.AddField(
            model_name='specialpack',
            name='img',
            field=models.ImageField(default='', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='specialpack',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='specialpack',
            name='nights',
            field=models.IntegerField(default='6'),
        ),
        migrations.AddField(
            model_name='specialpack',
            name='price',
            field=models.IntegerField(default='1000'),
        ),
    ]
