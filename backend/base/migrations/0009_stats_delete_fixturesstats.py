# Generated by Django 4.0.1 on 2022-01-16 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_fixturesstats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shots_on_goal', models.IntegerField(null=True)),
                ('shots_off_goal', models.IntegerField(null=True)),
                ('total_shots', models.IntegerField(null=True)),
                ('blocked_shots', models.IntegerField(null=True)),
                ('shots_insidebox', models.IntegerField(null=True)),
                ('shots_outsidebox', models.IntegerField(null=True)),
                ('fouls', models.IntegerField(null=True)),
                ('corner_kicks', models.IntegerField(null=True)),
                ('offsides', models.IntegerField(null=True)),
                ('ball_possesion', models.CharField(max_length=100, null=True)),
                ('yellow_cards', models.IntegerField(null=True)),
                ('red_cards', models.IntegerField(null=True)),
                ('goalkeeper_saves', models.IntegerField(null=True)),
                ('total_passes', models.IntegerField(null=True)),
                ('passes_accurate', models.IntegerField(null=True)),
                ('fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.fixtures')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.team')),
            ],
        ),
        migrations.DeleteModel(
            name='FixturesStats',
        ),
    ]
