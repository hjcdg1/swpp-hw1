# Generated by Django 2.1.7 on 2019-03-18 11:10

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
            name='Meeting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sinceWhen', models.DateTimeField()),
                ('tillWhen', models.DateTimeField()),
                ('highlighted', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id', 'created', 'sinceWhen', 'tillWhen', 'user'),
            },
        ),
    ]
