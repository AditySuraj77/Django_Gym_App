# Generated by Django 5.0.6 on 2024-07-16 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authapp', '0002_enrollment_membershipplan_trainer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='Price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='membershipplan',
            name='Price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='Salary',
            field=models.IntegerField(),
        ),
    ]
