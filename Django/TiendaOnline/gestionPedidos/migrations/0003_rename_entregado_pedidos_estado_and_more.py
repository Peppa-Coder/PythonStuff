# Generated by Django 4.1.4 on 2023-01-09 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0002_alter_clientes_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedidos',
            old_name='entregado',
            new_name='estado',
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.CharField(max_length=9, verbose_name='celular'),
        ),
    ]
