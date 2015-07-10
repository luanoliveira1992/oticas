# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClasseItem',
            fields=[
                ('codigo', models.AutoField(serialize=False, primary_key=True)),
                ('descricao', models.CharField(max_length=100, verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('codigo', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=255, verbose_name=b'Nome do Item')),
                ('tipo', models.IntegerField(verbose_name=b'Tipo Item', choices=[(0, b'Material'), (1, b'Servi\xc3\xa7o')])),
                ('classe', models.ForeignKey(verbose_name=b'Categoria', to='Item.ClasseItem')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('codigo', models.AutoField(serialize=False, primary_key=True)),
                ('descricao', models.CharField(max_length=255, verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
                ('observacao', models.TextField(verbose_name=b'Observa\xc3\xa7\xc3\xa3o')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='marca',
            field=models.ForeignKey(verbose_name=b'Marca', to='Item.Marca'),
        ),
    ]
