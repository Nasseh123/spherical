# Generated by Django 4.0.4 on 2022-05-22 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0050_alter_employee_emp_id_employeecouponpdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp379', max_length=70),
        ),
    ]