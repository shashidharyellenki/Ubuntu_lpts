# Generated by Django 4.0.6 on 2022-08-31 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directoryPage', '0005_units_content_difficulty_units_content_grades_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='units_content',
            name='Grades',
            field=models.CharField(choices=[('complete', 'complete'), ('Doubt', 'Doubt'), ('Incomplete', 'Incomplete')], max_length=100, null=True),
        ),
    ]
