from django.db import models
from common.models import CommonModel
from users.models import User

# Create your models here.
class Video(CommonModel):
  title = models.CharField(max_length=225)
  link = models.URLField()
  desciption = models.TextField(blank=True)
  category = models.CharField(max_length=225)
  view_count = models.PositiveIntegerField(default=0)
  thumbnail = models.URLField()
  video_uploded_url = models.URLField()
  video_file = models.FileField(upload_to='storage/')
  
  user = models.ForeignKey(User, on_delete=models.CASCADE)
