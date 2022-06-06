# Generated by Django 4.0.4 on 2022-05-24 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0054_employeeadvancepayment_date_paid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concretecasting',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrms.employee'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp274', max_length=70),
        ),
    ]