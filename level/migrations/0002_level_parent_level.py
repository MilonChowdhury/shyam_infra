# Generated by Django 2.1 on 2018-08-27 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='parent_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='level.Level'),
        ),
    ]
