# Generated by Django 2.2.1 on 2019-05-28 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration_in_months',
            field=models.SmallIntegerField(),
        ),
    ]
