# Generated by Django 4.0.6 on 2022-07-31 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directoryPage', '0002_alter_course_continouscredits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='continousCredits',
            field=models.CharField(choices=[('SoftSkills', 'SoftSkills'), ('continousCredits-ss', 'continousCredits-ss'), ('continousCredits-ps', 'continousCredits-ps'), ('continousCredits-hk', 'continousCredits-hk'), ('Technical', 'Technical')], max_length=50),
        ),
    ]
