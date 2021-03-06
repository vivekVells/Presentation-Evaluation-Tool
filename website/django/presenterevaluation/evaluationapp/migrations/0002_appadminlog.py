# Generated by Django 2.0.4 on 2018-05-04 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluationapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_logged_in', models.CharField(max_length=100)),
                ('last_logged_out', models.CharField(blank=True, max_length=100, null=True)),
                ('appAdminUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluationapp.AppAdmin')),
            ],
        ),
    ]
