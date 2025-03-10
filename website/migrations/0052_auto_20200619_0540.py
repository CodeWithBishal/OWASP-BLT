# Generated by Django 3.0.7 on 2020-06-19 05:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0051_auto_20200613_1515"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="domain",
            name="subscription",
        ),
        migrations.AddField(
            model_name="hunt",
            name="description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="subscription",
            name="domains_per_month",
            field=models.IntegerField(blank=True, default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subscription",
            name="hunt_per_domain",
            field=models.IntegerField(blank=True, default=2),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("url", models.URLField()),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("twitter", models.CharField(blank=True, max_length=30, null=True)),
                ("facebook", models.URLField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "subscription",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="website.Subscription",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="domain",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="website.Company",
            ),
        ),
    ]
