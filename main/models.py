from django.db import models
from core.models import TimeStampedModel

# Create your models here.


class User(TimeStampedModel):
    class Meta:
        db_table = "user_info"

    user_id = models.CharField(primary_key=True, max_length=100, verbose_name="사용자 아이디")
    user_password = models.CharField(max_length=100, verbose_name="사용자 비밀번호")
    user_nickname = models.CharField(max_length=100, verbose_name="사용자 별명")
    user_level = models.IntegerField(default=0, verbose_name="사용자 레벨")
    user_experience = models.IntegerField(default=0, verbose_name="사용자 경험치")

    def __str__(self):
        return self.user_id
