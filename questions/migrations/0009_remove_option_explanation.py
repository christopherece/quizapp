# Generated by Django 4.2.1 on 2023-05-31 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_question_explanation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='explanation',
        ),
    ]
