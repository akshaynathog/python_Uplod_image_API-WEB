# Generated by Django 4.1.1 on 2023-01-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0002_questions_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='created_date',
            field=models.DateField(auto_created=True, null=True),
        ),
    ]