# Generated by Django 5.1.3 on 2024-12-21 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Status',
            field=models.CharField(default='MP', max_length=3),
        ),
    ]
