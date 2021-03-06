# Generated by Django 2.2.2 on 2019-06-20 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('img_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='DrinkReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drinkreviews.Drink')),
            ],
        ),
    ]
