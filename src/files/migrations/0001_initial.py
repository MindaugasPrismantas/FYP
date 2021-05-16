# Generated by Django 3.2 on 2021-05-05 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(blank=True, max_length=255)),
                ('info', models.TextField(max_length=100)),
                ('document', models.FileField(upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]