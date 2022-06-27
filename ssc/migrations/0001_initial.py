# Generated by Django 4.0.5 on 2022-06-13 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=10)),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
