# Generated by Django 3.2 on 2021-05-11 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_alter_upload_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='document',
            field=models.FileField(upload_to='files'),
        ),
    ]
