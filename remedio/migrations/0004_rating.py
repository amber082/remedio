# Generated by Django 2.1 on 2018-11-25 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remedio', '0003_presc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=255, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'rating',
            },
        ),
    ]
