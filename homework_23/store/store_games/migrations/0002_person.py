# Generated by Django 4.2 on 2023-05-01 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]