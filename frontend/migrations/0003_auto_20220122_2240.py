# Generated by Django 3.2.4 on 2022-01-22 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_alter_users_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='room_id',
        ),
        migrations.AddField(
            model_name='users',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='frontend.rooms'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(max_length=16)),
                ('song_id', models.CharField(max_length=16)),
                ('artist', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('album', models.CharField(max_length=255)),
                ('duration', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.users')),
            ],
        ),
    ]
