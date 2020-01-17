# Generated by Django 2.2 on 2020-01-17 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('total', models.DecimalField(decimal_places=2, max_digits=7)),
                ('paid', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
