# Generated by Django 5.0.6 on 2024-12-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField(max_length=30)),
                ('father', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=200)),
                ('aducation', models.CharField(choices=[('7th ', '7th'), ('8th ', '8th'), ('9th ', '9th'), ('10th ', '10th'), ('11th ', '11th'), ('12th ', '12th')], max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]