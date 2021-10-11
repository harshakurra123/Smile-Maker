# Generated by Django 3.2.7 on 2021-10-08 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Joke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joke_title', models.CharField(blank=True, max_length=50)),
                ('joke_description', models.CharField(blank=True, max_length=500)),
                ('joke_likes', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('joke_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joke_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'joke',
            },
        ),
    ]
