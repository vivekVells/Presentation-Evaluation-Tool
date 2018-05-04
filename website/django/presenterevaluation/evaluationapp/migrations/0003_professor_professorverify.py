# Generated by Django 2.0.4 on 2018-05-04 15:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('evaluationapp', '0002_appadminlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=70)),
                ('mailId', models.CharField(max_length=70)),
                ('accesscode', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('recovery_answer', models.CharField(max_length=20)),
                ('last_updated_on', models.DateTimeField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=70)),
                ('middle_name', models.CharField(blank=True, default='', max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_on', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessorVerify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailId', models.CharField(max_length=70)),
            ],
        ),
    ]
