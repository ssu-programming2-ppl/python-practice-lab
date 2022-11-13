from django.db import models
from core.models import TimeStampedModel


class Board(TimeStampedModel):
    class Meta:
        db_table = "board_info"

    board_seq = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="게시판 번호"
    )
    board_title = models.CharField(max_length=150, verbose_name="게시판 제목")
    board_view_count = models.IntegerField(verbose_name="게시판 조회수 카운팅")
    borad_link = models.CharField(max_length=150, verbose_name="게시판 링크")
    user_id = models.CharField(max_length=150, verbose_name="사용자(작성자) 아이디")

    def __str__(self):
        return self.board_seq
