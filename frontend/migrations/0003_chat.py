# Generated by Django 3.2.4 on 2022-09-22 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20220919_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=16)),
                ('message', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.rooms')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='frontend.users')),
            ],
        ),
    ]