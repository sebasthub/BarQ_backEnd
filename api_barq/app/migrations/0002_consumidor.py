# Generated by Django 4.2 on 2023-05-03 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('valido_ate', models.DateTimeField(auto_now_add=True)),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.mesa')),
            ],
        ),
    ]
