# Generated by Django 3.2.3 on 2022-04-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp750', max_length=70),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
