# Generated by Django 4.1.1 on 2023-01-19 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0006_alter_questions_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='created_date',
        ),
    ]