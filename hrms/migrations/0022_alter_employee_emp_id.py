# Generated by Django 4.0.4 on 2022-05-11 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0021_alter_employee_emp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp640', max_length=70),
        ),
    ]