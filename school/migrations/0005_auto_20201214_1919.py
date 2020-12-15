# Generated by Django 3.0 on 2020-12-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_auto_20201214_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='time',
            name='time',
            field=models.CharField(default='9.30', max_length=100),
        ),
    ]
