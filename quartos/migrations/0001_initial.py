# Generated by Django 5.0.1 on 2024-02-05 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quarto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_quarto', models.PositiveSmallIntegerField(unique=True, verbose_name='Número do quarto')),
                ('tipo_quarto', models.CharField(choices=[('SIMPLES', 'Quarto simples'), ('PADRAO', 'Quarto padrão do hotel'), ('LUXO', 'Quarto luxuoso')], default='PADRAO', max_length=10, verbose_name='Tipo de quarto para hospedagem')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='quarto_img/')),
                ('descricao_quarto', models.TextField()),
            ],
            options={
                'verbose_name': 'Quarto',
                'verbose_name_plural': 'Quartos',
                'db_table': 'quarto',
            },
        ),
    ]
