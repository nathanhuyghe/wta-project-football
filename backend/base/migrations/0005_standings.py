# Generated by Django 4.0.1 on 2022-01-14 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_team_form_remove_team_goals_diff_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Standings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('form', models.CharField(max_length=100)),
                ('rank', models.IntegerField()),
                ('played', models.IntegerField()),
                ('win', models.IntegerField()),
                ('draw', models.IntegerField()),
                ('loss', models.IntegerField()),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.league')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.team')),
            ],
        ),
    ]
