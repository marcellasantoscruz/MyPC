# Generated by Django 4.0.4 on 2022-05-16 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessadorIniciante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.TextField()),
                ('alternativa_1', models.TextField()),
                ('alternativa_2', models.TextField()),
                ('alternativa_3', models.TextField()),
                ('alternativa_4', models.TextField()),
                ('resposta', models.TextField()),
            ],
        ),
    ]
