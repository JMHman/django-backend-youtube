from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video


# Create your models here.
class Notification(CommonModel):
  message = models.CharField(max_length=255)
  is_read = models.BooleanField(default=False)

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  video = models.ForeignKey(Video, on_delete=models.SET_NULL)

  # user:notification => 1:N, N:N, 1:1
  # video:notification => 1:N