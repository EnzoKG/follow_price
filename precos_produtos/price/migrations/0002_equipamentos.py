# Generated by Django 2.2.1 on 2021-03-17 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='nulo', max_length=200)),
                ('nome', models.CharField(default='nulo', max_length=200)),
            ],
        ),
    ]