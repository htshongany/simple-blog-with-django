# Generated by Django 4.0.6 on 2022-08-06 17:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blogpost_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='update_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
