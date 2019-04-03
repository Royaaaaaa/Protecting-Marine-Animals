# Generated by Django 2.1.7 on 2019-04-03 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APP01', '0002_animal_adetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latAnimal', models.FloatField(blank=True, default=None, null=True)),
                ('lonAnimal', models.FloatField(blank=True, default=None, null=True)),
                ('lAnimal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP01.Animal')),
            ],
        ),
    ]