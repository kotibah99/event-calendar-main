# Generated by Django 3.1.12 on 2021-07-17 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("calendarapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="events",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="eventmember",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="events",
                to="calendarapp.event",
            ),
        ),
        migrations.AlterField(
            model_name="eventmember",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="event_members",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

