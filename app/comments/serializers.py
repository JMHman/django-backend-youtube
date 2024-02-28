from rest_framework.serializer import ModelSerializer
from .models import Comment

class CommentSerializer(ModelSerializer):
  class Meta:
    model = Comment
    # fields = ('id', 'user','like', 'dislike', 'content')
    fields = '__all'