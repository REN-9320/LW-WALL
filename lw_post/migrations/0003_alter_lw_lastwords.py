# Generated by Django 5.1.2 on 2024-11-13 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lw_post', '0002_remove_lw_age_remove_lw_country_remove_lw_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lw',
            name='lastwords',
            field=models.CharField(max_length=500),
        ),
    ]