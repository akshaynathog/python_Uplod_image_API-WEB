# Generated by Django 4.1.1 on 2023-01-19 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0005_alter_questions_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]