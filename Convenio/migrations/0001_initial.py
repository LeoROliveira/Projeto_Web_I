# Generated by Django 4.0.5 on 2022-06-15 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convenio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=100)),
                ('CNPJ', models.CharField(max_length=100)),
                ('Contrato', models.CharField(max_length=100)),
                ('Data_adesão', models.DateField(max_length=100)),
                ('Data_término', models.DateField(max_length=100)),
            ],
        ),
    ]
