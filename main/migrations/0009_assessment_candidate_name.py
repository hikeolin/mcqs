# Generated by Django 3.1.1 on 2020-10-02 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20201001_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='candidate_name',
            field=models.CharField(default='anonymous', max_length=30),
        ),
    ]