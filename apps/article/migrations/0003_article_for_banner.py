# Generated by Django 5.0.4 on 2024-04-21 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='for_banner',
            field=models.BooleanField(default=False),
        ),
    ]
