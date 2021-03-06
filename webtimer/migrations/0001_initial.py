# Generated by Django 3.0.8 on 2020-07-11 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Webtimer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, null=True)),
                ('urls', models.CharField(max_length=120, null=True)),
                ('time', models.DecimalField(decimal_places=3, max_digits=1000, null=True)),
                ('summary', models.TextField(null=True)),
                ('featured', models.BooleanField(default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loadtime', models.DecimalField(decimal_places=3, max_digits=1000, null=True)),
                ('captured_date', models.DateTimeField(null=True)),
                ('webtimer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webtimer.Webtimer')),
            ],
        ),
    ]
