# Generated by Django 2.2 on 2020-03-11 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chintucongtua', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='linhnhixinhdep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choiceDay', models.CharField(max_length=100)),
                ('choiceTime', models.CharField(max_length=100)),
                ('voterName', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
