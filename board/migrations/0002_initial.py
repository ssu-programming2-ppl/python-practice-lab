# Generated by Django 4.1.2 on 2022-12-12 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("board", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="user_id",
            field=models.ForeignKey(
                db_column="user_id",
                db_constraint=False,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="user_board",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
