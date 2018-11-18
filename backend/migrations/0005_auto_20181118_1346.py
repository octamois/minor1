# Generated by Django 2.1.3 on 2018-11-18 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20181118_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='q_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=10)),
                ('fname', models.CharField(max_length=50)),
                ('batch', models.CharField(max_length=2)),
                ('quiz_instance', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=10)),
                ('ques', models.CharField(max_length=150)),
                ('opt1', models.CharField(max_length=50)),
                ('opt2', models.CharField(max_length=50)),
                ('opt3', models.CharField(max_length=50)),
                ('opt4', models.CharField(max_length=50)),
                ('correct', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='quiz_available',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_name', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='S_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('userid', models.IntegerField(unique=True)),
                ('batch', models.CharField(max_length=2)),
                ('subject_code', models.CharField(max_length=10)),
                ('marks', models.IntegerField()),
                ('quiz_instance', models.CharField(max_length=4)),
            ],
        ),
        migrations.DeleteModel(
            name='details',
        ),
        migrations.AlterField(
            model_name='auth',
            name='userid',
            field=models.IntegerField(unique=True),
        ),
    ]