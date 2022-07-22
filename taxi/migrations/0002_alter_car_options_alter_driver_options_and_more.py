# Generated by Django 4.0.5 on 2022-07-22 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['model']},
        ),
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ['username'], 'verbose_name': 'driver', 'verbose_name_plural': 'drivers'},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='driver',
            name='license_number',
            field=models.CharField(max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='country',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
