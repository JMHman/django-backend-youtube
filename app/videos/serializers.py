from rest_framework.serializer import ModelSerializer
from .models import Video
from users.serializers import UserSelializer
from comments.serializers import CommentSelializer



class VideoSerializer(ModelSerializer):
  user = UserSelializer
  comment_set = CommentSelializer
  
  class Meta:
    model = Video
    fields = '__all__' # video 모델의 전체를 보여줘