# Generated by Django 2.1 on 2020-04-30 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200430_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='body',
            field=models.IntegerField(verbose_name=(0, 1, 2, 3, 4)),
        ),
    ]
