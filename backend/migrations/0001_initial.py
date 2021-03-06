# Generated by Django 2.1.1 on 2018-11-18 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.DecimalField(decimal_places=2, max_digits=10, unique=True)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('userid', models.DecimalField(decimal_places=2, max_digits=10, unique=True)),
                ('batch', models.CharField(max_length=2)),
                ('subject_code', models.CharField(max_length=10)),
                ('marks', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=10)),
                ('subject_code', models.CharField(max_length=10)),
            ],
        ),
    ]
