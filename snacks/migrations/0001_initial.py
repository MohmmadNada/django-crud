# Generated by Django 3.2.5 on 2021-07-13 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('purchaser', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
        ),
    ]