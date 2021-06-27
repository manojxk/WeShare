# Generated by Django 3.2.4 on 2021-06-27 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_notes_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='branch',
            field=models.CharField(choices=[('Aerospace Engineering', 'Aerospace Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Computer Science & Engineering', 'Computer Science & Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Metallurgical Engineering & Materials Science', 'Metallurgical Engineering & Materials Science')], max_length=50),
        ),
        migrations.AlterField(
            model_name='notes',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]
