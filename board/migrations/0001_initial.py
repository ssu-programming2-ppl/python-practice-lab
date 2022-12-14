# Generated by Django 4.1.2 on 2022-12-12 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Board",
            fields=[
                (
                    "board_seq",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="게시판 번호",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "board_title",
                    models.CharField(max_length=150, verbose_name="게시판 제목"),
                ),
                ("board_view_count", models.IntegerField(verbose_name="게시판 조회수 카운팅")),
                ("board_link", models.CharField(max_length=150, verbose_name="게시판 링크")),
                (
                    "board_division",
                    models.CharField(max_length=150, verbose_name="게시판 구분"),
                ),
            ],
            options={
                "db_table": "board_info",
            },
        ),
    ]
