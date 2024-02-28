from django.db import models
from common.models import CommonModel
from users.models import User


# Create your models here.
class Subxcription(CommonModel):
  subscriber = models.ForeignKey(User, on_delete=models.CASCADE)
  subscribed_to = models.ForeignKey(User, on_delete=models.CASCADE)