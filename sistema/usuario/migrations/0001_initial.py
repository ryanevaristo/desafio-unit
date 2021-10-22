# Generated by Django 3.2.8 on 2021-10-20 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificado', models.FileField(upload_to='media/')),
                ('atividade', models.CharField(max_length=200)),
                ('quant_horas', models.CharField(max_length=20, verbose_name='Quantidade de Horas')),
                ('status', models.CharField(choices=[('H', 'Homologado'), ('N', 'Não-Homologado')], max_length=1)),
            ],
        ),
    ]
