# Generated by Django 4.1.1 on 2022-10-12 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0002_dummy'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='notes',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
