# Generated by Django 3.2.4 on 2021-06-26 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsms', '0002_alter_students_reg_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students_reg',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
