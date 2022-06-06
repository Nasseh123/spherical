# Generated by Django 4.0.4 on 2022-05-24 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0059_alter_employee_emp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp582', max_length=70),
        ),
        migrations.AlterField(
            model_name='employeechat',
            name='sender',
            field=models.CharField(choices=[('employer', 'employer'), ('employee', 'employee')], default='employer', max_length=15),
        ),
    ]
