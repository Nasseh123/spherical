# Generated by Django 4.0.4 on 2022-05-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0023_alter_employee_emp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp754', max_length=70),
        ),
    ]