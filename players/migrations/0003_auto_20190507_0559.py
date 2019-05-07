# Generated by Django 2.1.7 on 2019-05-07 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('players', '0002_library'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerGroup',
            fields=[
                ('PLAYER_P_GROUP_ID', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('P_GROUP_ID', models.IntegerField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='player_group',
            name='username',
        ),
        migrations.DeleteModel(
            name='Player_Group',
        ),
    ]
