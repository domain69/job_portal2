# Generated by Django 2.2a1 on 2019-04-04 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=30)),
                ('comp_username', models.CharField(max_length=20)),
                ('comp_password', models.CharField(max_length=16)),
                ('comp_phoneno', models.CharField(max_length=13)),
                ('comp_email', models.EmailField(max_length=100)),
                ('comp_description', models.CharField(max_length=300)),
                ('comp_addressline1', models.CharField(max_length=100)),
                ('comp_addressline2', models.CharField(max_length=100)),
                ('comp_zipcode', models.CharField(max_length=20)),
                ('comp_state', models.CharField(max_length=100)),
                ('comp_country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jobfield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_description', models.CharField(max_length=300)),
                ('job_category', models.CharField(max_length=100)),
                ('job_experience', models.CharField(max_length=20)),
                ('job_location', models.CharField(max_length=50)),
                ('job_salary', models.CharField(max_length=100)),
                ('job_postedon', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('job_comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.Company')),
            ],
        ),
    ]