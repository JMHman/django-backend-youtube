from rest_framework.serializer import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'email')