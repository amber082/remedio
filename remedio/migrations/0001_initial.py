# Generated by Django 2.1 on 2018-08-27 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dis',
            fields=[
                ('disid', models.IntegerField(primary_key=True, serialize=False)),
                ('disease', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'dis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Relate',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('symid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'relate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Symp',
            fields=[
                ('symid', models.IntegerField(primary_key=True, serialize=False)),
                ('symptom', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'symp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sympdis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom', models.CharField(blank=True, max_length=255, null=True)),
                ('disease', models.CharField(blank=True, max_length=255, null=True)),
                ('medicine', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'sympdis',
                'managed': False,
            },
        ),
    ]
