# Generated by Django 3.0.7 on 2020-09-24 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("experiments", "0113_auto_20200923_2021"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="nimbusexperiment",
            name="bugzilla_id",
        ),
    ]