# Generated by Django 2.1.3 on 2018-11-26 17:25

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chamada', '0002_turma_ano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamada',
            name='ativa',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='chamada',
            name='data',
            field=models.DateField(default=datetime.datetime(2018, 11, 26, 17, 25, 42, 87196, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='chamada',
            name='turma_aluno',
            field=models.ManyToManyField(related_name='turma_aluno', through='chamada.Presenca', to='chamada.TurmaAluno'),
        ),
        migrations.AlterField(
            model_name='turmaaluno',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turma', to='chamada.Turma'),
        ),
    ]
