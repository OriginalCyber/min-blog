# Generated by Django 3.2.5 on 2021-09-04 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_category_student_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='Student',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='web.Student'),
        ),
    ]
