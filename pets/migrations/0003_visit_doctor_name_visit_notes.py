# Generated by Django 5.1.3 on 2024-11-15 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_alter_visit_visit_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='doctor_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
