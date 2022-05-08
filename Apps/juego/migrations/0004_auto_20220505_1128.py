# Generated by Django 3.2.8 on 2022-05-05 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0003_auto_20220504_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuesta',
            name='correcta',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='respuesta',
            name='pregunta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='juego.pregunta'),
        ),
        migrations.DeleteModel(
            name='Tarjeta',
        ),
    ]