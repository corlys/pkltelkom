# Generated by Django 3.0.8 on 2020-08-07 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtimer', '0003_auto_20200801_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webtimer',
            name='time',
            field=models.DecimalField(decimal_places=3, max_digits=65, null=True),
        ),
    ]
