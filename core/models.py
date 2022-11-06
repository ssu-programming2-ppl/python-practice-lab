from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):

    """This is TimeStamped Model"""

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # abstract가 True면 DB에는 등록되지 않습니다.
    class Meta:
        abstract = True