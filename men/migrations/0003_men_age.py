# Generated by Django 4.0.6 on 2022-07-27 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0002_alter_men_year_of_death'),
    ]

    operations = [
        migrations.AddField(
            model_name='men',
            name='age',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Age'),
        ),
    ]
