# Generated by Django 2.2 on 2020-03-11 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choiceDay', models.CharField(max_length=100)),
                ('choiceTime', models.IntegerField()),
                ('voterName', models.CharField(max_length=100)),
            ],
        ),
    ]
