from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video

# Create your models here.
class Reaction(CommonModel):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  video = models.ForeignKey(Video, on_delete=models.CASCADE)
  
  # boolean: True, False, None(x)
  # like = models.BoolenField(default=False)
  # dislike = models.BoolenField(default=False)
  LIKE = 'like'
  DISLIKE = 'dislike'
  NO_REACTION = 'no_reaction'

  REACTION_CHOICES = (
    (LIKE, 'like'),
    (DISLIKE, 'dislike'),
    (NO_REACTION, 'No reaction'),
  )

  reaction = models.IntegerField(
    choices=REACTION_CHOICES,
    default=NO_REACTION
  )