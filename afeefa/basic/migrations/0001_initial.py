# Generated by Django 5.1.3 on 2024-12-17 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('S_NO', models.IntegerField(primary_key=True, serialize=False)),
                ('NAME', models.CharField(max_length=40)),
                ('AGE', models.IntegerField()),
            ],
        ),
    ]
