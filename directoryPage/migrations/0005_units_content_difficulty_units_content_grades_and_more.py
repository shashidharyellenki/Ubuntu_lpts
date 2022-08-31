# Generated by Django 4.0.6 on 2022-08-30 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directoryPage', '0004_remove_units_content_units_uc_relation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='units_content',
            name='Difficulty',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Advanced', 'Advanced')], default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='units_content',
            name='Grades',
            field=models.CharField(choices=[('Enrolled', 'Enrolled'), ('Mastery', 'Mastery'), ('Exemplary', 'Exemplary'), ('Incomplete', 'Incomplete'), ('Pending', 'Pending')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='units_content',
            name='Remarks',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
