# Generated by Django 2.0 on 2017-12-16 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0005_countriestempmeanvalue_countriestempminvalue'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountriesRainfallValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uMonthId', models.IntegerField()),
                ('uValue', models.DecimalField(decimal_places=2, max_digits=6)),
                ('uCountryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helloworld.Country')),
            ],
        ),
        migrations.CreateModel(
            name='CountriesSunshineValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uMonthId', models.IntegerField()),
                ('uValue', models.DecimalField(decimal_places=2, max_digits=6)),
                ('uCountryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helloworld.Country')),
            ],
        ),
        migrations.RenameField(
            model_name='countriestempmaxvalue',
            old_name='uTempValue',
            new_name='uValue',
        ),
        migrations.RenameField(
            model_name='countriestempmeanvalue',
            old_name='uTempValue',
            new_name='uValue',
        ),
        migrations.RenameField(
            model_name='countriestempminvalue',
            old_name='uTempValue',
            new_name='uValue',
        ),
        migrations.RemoveField(
            model_name='countriestempmaxvalue',
            name='id',
        ),
        migrations.AlterField(
            model_name='countriestempmaxvalue',
            name='uMonthId',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
