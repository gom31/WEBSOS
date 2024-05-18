# Generated by Django 4.2.11 on 2024-05-17 03:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("question", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="examlog",
            name="username",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="userWhoSolved",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="solvedquestions",
            name="submitted_answer",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="solvedquestions",
            name="username",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="userWhoHadSolved",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="solvedquestions",
            unique_together={("username", "solvedQuestions")},
        ),
    ]
