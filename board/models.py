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
    board_link = models.CharField(max_length=150, verbose_name="게시판 링크")
    board_division = models.CharField(max_length=150, verbose_name="게시판 구분")
    # user_id = models.CharField(max_length=150, verbose_name="사용자(작성자) 아이디")
    user_id = models.ForeignKey('main.User', db_constraint=False,
                                on_delete=models.DO_NOTHING, db_column="user_id", related_name="user_board")

    def __str__(self):
        return self.board_seq
