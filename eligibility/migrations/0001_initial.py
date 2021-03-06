# Generated by Django 2.1 on 2018-08-25 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialEligibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_capacity', models.TextField(blank=True, null=True)),
                ('turn_over', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('key_word_value', models.CharField(blank=True, max_length=255, null=True)),
                ('net_worth', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('other', models.TextField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.ProjectDetails')),
            ],
        ),
        migrations.CreateModel(
            name='InitialCosting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('status', models.BooleanField(default=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.ProjectDetails')),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalEligibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('construction_work_experience', models.CharField(blank=True, max_length=255, null=True)),
                ('key_work_experience', models.TextField(blank=True, null=True)),
                ('similar_nature_of_work', models.TextField(blank=True, null=True)),
                ('machinery_list', models.TextField(blank=True, null=True)),
                ('others', models.TextField(blank=True, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.ProjectDetails')),
            ],
        ),
    ]
