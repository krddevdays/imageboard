# Generated by Django 2.1 on 2019-01-11 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageboard', '0006_auto_20181225_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='checksum',
            field=models.CharField(blank=True, editable=False, max_length=32),
        ),
    ]
