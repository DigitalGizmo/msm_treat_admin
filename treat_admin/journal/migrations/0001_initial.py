# Generated by Django 2.0.13 on 2019-11-20 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=48, unique=True, verbose_name='short name')),
                ('title', models.CharField(max_length=64)),
                ('entry_date', models.DateField()),
                ('ordinal', models.IntegerField(blank=True, verbose_name='sequence in day')),
                ('lat', models.FloatField(verbose_name='latitude')),
                ('lon', models.FloatField(verbose_name='longitude')),
                ('zoom_level', models.IntegerField(default=10)),
                ('is_fippable', models.BooleanField(default=False, verbose_name='Allow image flip')),
                ('entry_text', models.TextField(blank=True, default='')),
            ],
        ),
    ]
