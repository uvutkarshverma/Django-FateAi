# Generated by Django 4.2.1 on 2023-07-05 16:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_aitools_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aitools',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='aitools',
            name='current_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]