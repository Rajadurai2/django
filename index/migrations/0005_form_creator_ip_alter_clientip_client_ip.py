# Generated by Django 4.0.2 on 2023-04-16 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_clientip_hostip'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='creator_ip',
            field=models.CharField(default=1, max_length=30),
        ),
        migrations.AlterField(
            model_name='clientip',
            name='client_ip',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='client_ip', to='index.form'),
        ),
    ]
