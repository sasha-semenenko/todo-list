# Generated by Django 4.2.9 on 2024-02-02 18:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task_and_tags", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tasks",
            name="tags",
            field=models.ManyToManyField(related_name="tags", to="task_and_tags.tag"),
        ),
    ]
