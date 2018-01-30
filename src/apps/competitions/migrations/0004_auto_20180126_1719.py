# Generated by Django 2.0.1 on 2018-01-26 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0003_auto_20180125_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitionparticipant',
            name='competition',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='competitions.Competition'),
        ),
        migrations.AlterField(
            model_name='page',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='competitions.Competition'),
        ),
        migrations.AlterField(
            model_name='phase',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phases', to='competitions.Competition'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='phase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='competitions.Phase'),
        ),
    ]