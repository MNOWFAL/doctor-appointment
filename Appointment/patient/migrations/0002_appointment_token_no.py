# Generated by Django 5.0.6 on 2024-07-10 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='token_no',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
