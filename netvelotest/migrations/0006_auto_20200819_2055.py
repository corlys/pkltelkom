# Generated by Django 3.0.8 on 2020-08-19 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netvelotest', '0005_auto_20200807_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speedhistory',
            name='download',
            field=models.DecimalField(decimal_places=0, max_digits=65, null=True),
        ),
    ]
