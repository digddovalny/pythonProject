# Generated by Django 5.0.1 on 2024-02-11 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]