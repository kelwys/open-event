# Generated by Django 2.2.4 on 2019-08-17 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0004_palestrante_social_midia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_palestra', models.CharField(max_length=20, verbose_name='Nome da Palestra')),
                ('date', models.DateField(verbose_name='Data')),
                ('time', models.TimeField(verbose_name='Hora')),
                ('arquivo', models.FileField(upload_to='uploads/', verbose_name='arquivo')),
                ('palestrante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='evento.Palestrante')),
            ],
            options={
                'verbose_name': 'Agenda',
                'verbose_name_plural': 'Agendas',
            },
        ),
    ]
