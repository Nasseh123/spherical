# Generated by Django 4.0.4 on 2022-05-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0047_alter_employee_emp_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expenses',
            old_name='date_creaed',
            new_name='date_created',
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp611', max_length=70),
        ),
    ]
