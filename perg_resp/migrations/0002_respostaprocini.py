# Generated by Django 4.0.4 on 2022-05-23 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perg_resp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RespostaProcIni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.TextField()),
            ],
        ),
    ]
