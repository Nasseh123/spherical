# Generated by Django 3.2.3 on 2022-04-27 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0011_alter_employee_emp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp728', max_length=70),
        ),
    ]
