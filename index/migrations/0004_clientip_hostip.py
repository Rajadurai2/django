# Generated by Django 4.0.2 on 2023-04-16 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_remove_form_see_response'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_ip', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Hostip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_ip', models.CharField(max_length=30)),
            ],
        ),
    ]
