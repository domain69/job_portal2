# Generated by Django 2.2a1 on 2019-04-10 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobseeker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('contact', models.IntegerField(verbose_name=15)),
                ('address', models.TextField(max_length=800)),
                ('max_Qualification', models.CharField(max_length=150)),
            ],
        ),
    ]
