# Generated by Django 5.0.6 on 2024-07-19 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coarse',
            fields=[
                ('coarse_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('duration', models.DateField()),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
