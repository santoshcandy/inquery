# Generated by Django 5.0.6 on 2024-06-26 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('PhoneNumber', models.CharField(max_length=10)),
                ('Location', models.CharField(max_length=20)),
            ],
        ),
    ]
