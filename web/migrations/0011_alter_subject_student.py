# Generated by Django 3.2.7 on 2021-09-08 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_rename_student_subject_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='student',
            field=models.ManyToManyField(blank=True, default=None, to='web.Student'),
        ),
    ]
