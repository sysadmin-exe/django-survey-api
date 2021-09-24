# Generated by Django 3.2.6 on 2021-09-23 07:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surveyQuestion', models.CharField(max_length=240)),
                ('surveyOptions', models.JSONField(default=None)),
                ('CreatedAt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surveyAnswer', models.CharField(max_length=240)),
                ('CreatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('surveyQuestion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.surveyquestion')),
            ],
        ),
    ]