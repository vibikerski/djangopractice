# Generated by Django 5.0.1 on 2024-01-25 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('creation_year', models.IntegerField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=4)),
                ('genre', models.ManyToManyField(related_name='games', to='lesson.genre')),
            ],
        ),
    ]
