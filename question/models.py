from django.db import models
from core.models import TimeStampedModel


class Question(TimeStampedModel):
    class Meta:
        db_table = "question_info"

    question_seq = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="문제 번호"
    )
    question_title = models.CharField(max_length=150, verbose_name="문제 제목")
    question_level = models.CharField(max_length=150, verbose_name="문제 레벨")
    question_lang = models.CharField(max_length=150, verbose_name="문제 언어")
    question_text = models.TextField(verbose_name="문제 내용")
    question_code = models.TextField(verbose_name="문제 정답 코드")
    # user_id = models.CharField(max_length=150, verbose_name="사용자(작성자) 아이디")
    # user_id = models.ForeignKey('main.User', db_constraint=False, on_delete=models.DO_NOTHING, db_column="user_id", related_name="user_question")
    user_id = models.ManyToManyField('main.User', through='UserQuestionMap')

    def __str__(self):
        return str(self.question_seq)


class Testcase(TimeStampedModel):
    class Meta:
        db_table = "testcase_info"

    testcase_seq = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="테스트 케이스 번호"
    )
    testcase_input = models.TextField(verbose_name="테스트 케이스 입력값")
    testcase_output = models.TextField(verbose_name="테스트 케이스 출력값")
    testcase_open_yn = models.CharField(max_length=2, verbose_name="테스트 케이스 공개 여부")
    # question_seq = models.IntegerField(verbose_name="문제 번호")
    question_seq = models.ForeignKey(Question, db_constraint=False, on_delete=models.CASCADE, db_column="question_seq", related_name="question_testcase")

    def __str__(self):
        return self.testcase_seq


class UserQuestionMap(TimeStampedModel):
    class Meta:
        db_table = "user_question_map"

    map_seq = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="문제 번호"
    )
    user_id = models.ForeignKey('main.User', db_constraint=False, on_delete=models.CASCADE, db_column="user_id", related_name="user_map")
    question_seq = models.ForeignKey(Question, db_constraint=False, on_delete=models.CASCADE, db_column="question_seq", related_name="question_map")
    question_start_time = models.DateTimeField(null=True, verbose_name="문제 풀이 시작 시간")
    question_end_time = models.DateTimeField(null=True, verbose_name="문제 풀이 종료 시간")
    question_submit_count = models.IntegerField(default=0, verbose_name="문제 제출 카운팅")
    question_correct_yn = models.CharField(max_length=2, verbose_name="문제 정답 여부")
    question_save_yn = models.CharField(max_length=2, verbose_name="문제 저장 여부")
    question_rating = models.IntegerField(null=True, verbose_name="문제 별점")

    def __str__(self):
        return self.question_seq
