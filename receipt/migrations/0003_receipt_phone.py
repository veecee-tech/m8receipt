# Generated by Django 4.0.3 on 2022-03-30 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt', '0002_alter_receipt_receipt_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
