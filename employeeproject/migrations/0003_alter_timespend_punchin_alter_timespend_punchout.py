# Generated by Django 4.1.3 on 2022-11-07 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeproject', '0002_alter_timespend_punchin_alter_timespend_punchout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timespend',
            name='punchin',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timespend',
            name='punchout',
            field=models.DateField(blank=True, null=True),
        ),
    ]
