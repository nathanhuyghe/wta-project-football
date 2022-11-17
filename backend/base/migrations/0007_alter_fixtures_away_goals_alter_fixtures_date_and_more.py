# Generated by Django 4.0.1 on 2022-01-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_fixtures_remove_upcomingfixtures_awayteam_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixtures',
            name='away_goals',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='fixtures',
            name='date',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='fixtures',
            name='home_goals',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='fixtures',
            name='referee',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fixtures',
            name='status',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='fixtures',
            name='venue',
            field=models.CharField(max_length=300, null=True),
        ),
    ]