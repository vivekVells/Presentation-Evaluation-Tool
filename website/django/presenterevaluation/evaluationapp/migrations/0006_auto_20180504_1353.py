# Generated by Django 2.0.4 on 2018-05-04 17:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('evaluationapp', '0005_presenter_student_studentlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresenterNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewedby', models.CharField(max_length=70)),
                ('reviewedfor', models.CharField(default='', max_length=20)),
                ('eva', models.CharField(max_length=70)),
                ('com', models.CharField(max_length=500)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated_on', models.DateTimeField(blank=True, null=True)),
                ('deleted_on', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='presenter',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='presenter',
            name='deleted_on',
        ),
        migrations.RemoveField(
            model_name='presenter',
            name='last_updated_on',
        ),
        migrations.AddField(
            model_name='presenter',
            name='reviewedfor',
            field=models.CharField(default=django.utils.timezone.now, max_length=70),
            preserve_default=False,
        ),
    ]
