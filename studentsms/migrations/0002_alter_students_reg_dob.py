# Generated by Django 3.2.4 on 2021-06-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students_reg',
            name='dob',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
