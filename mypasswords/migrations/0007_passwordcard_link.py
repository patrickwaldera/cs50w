# Generated by Django 3.1.6 on 2022-09-20 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypasswords', '0006_auto_20220920_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwordcard',
            name='link',
            field=models.CharField(default='-', max_length=300),
            preserve_default=False,
        ),
    ]
