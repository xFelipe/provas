# Generated by Django 2.1 on 2019-04-10 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prova', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questao',
            name='resposta_correta',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prova.Resposta'),
        ),
    ]