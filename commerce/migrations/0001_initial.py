# Generated by Django 4.2.3 on 2023-07-23 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('marca', models.CharField(max_length=100)),
                ('preco', models.FloatField()),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(upload_to='images')),
            ],
        ),
    ]
