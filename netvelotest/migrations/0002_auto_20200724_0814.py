# Generated by Django 3.0.8 on 2020-07-24 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netvelotest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netvelocity',
            name='server',
            field=models.DecimalField(decimal_places=3, max_digits=65, null=True),
        ),
    ]
