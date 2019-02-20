# Generated by Django 2.1.7 on 2019-02-20 06:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Con',
            fields=[
                ('CON_ID', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('GAME_ID', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('PLAYER_ID', models.AutoField(primary_key=True, serialize=False)),
                ('REGISTER_DATE', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Player_Group',
            fields=[
                ('PLAYER_P_GROUP_ID', models.AutoField(primary_key=True, serialize=False)),
                ('PLAYER_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='session.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('ROUND_ID', models.AutoField(primary_key=True, serialize=False)),
                ('ROUND_BEGIN', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('SESSION_ID', models.AutoField(primary_key=True, serialize=False)),
                ('SESSION_BEGIN', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('CON_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='session.Con')),
                ('GAME_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='session.Game')),
            ],
        ),
        migrations.AddField(
            model_name='round',
            name='SESSION_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='session.Session'),
        ),
        migrations.AddField(
            model_name='con',
            name='CON_OWNER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='session.Player'),
        ),
    ]
