# Generated by Django 3.2.4 on 2021-07-02 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsms', '0005_students_reg_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students_reg',
            name='admin_no',
            field=models.CharField(blank=True, max_length=225, null=True, unique=True),
        ),
    ]
