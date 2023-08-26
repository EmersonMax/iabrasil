# Generated by Django 4.2.4 on 2023-08-18 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ferramentas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_curta', models.CharField(max_length=1000, null=True)),
                ('descricao_longa', models.CharField(max_length=1000, null=True)),
                ('opnioes', models.CharField(max_length=1000, null=True)),
                ('estrelas', models.IntegerField(null=True)),
                ('assinatura', models.CharField(max_length=1000, null=True)),
                ('valor_assinatura', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
            ],
        ),
    ]