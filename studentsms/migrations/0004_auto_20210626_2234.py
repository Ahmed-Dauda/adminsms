# Generated by Django 3.2.4 on 2021-06-26 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsms', '0003_alter_students_reg_dob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students_reg',
            old_name='addmin_no',
            new_name='admin_no',
        ),
        migrations.AddField(
            model_name='students_reg',
            name='house',
            field=models.CharField(blank=True, choices=[('red', 'red'), ('blue', 'blue'), ('yellow', 'yellow'), ('green', 'green')], max_length=225, null=True),
        ),
    ]
