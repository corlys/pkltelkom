# Generated by Django 3.0.8 on 2020-08-07 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netvelotest', '0003_speedhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='netvelocity',
            name='featured',
            field=models.BooleanField(default=True, null=True),
        ),
    ]