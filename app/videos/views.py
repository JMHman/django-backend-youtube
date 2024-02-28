from django.shortcuts import render
from rest_framework.view import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Video
from .serializers import VideoSerializer


# Create your views here.
# - VideoList
#   api/v1/videos
class VideoList(APIView):
#   - GET: 전체 비디오 목록 조회
  def get(self, request):
    videos = Video.objects.all()
    print('videos : ', videos) # 직렬화(장고객체->JSON으로 변환) => SERIALIZER
    serializer = VideoSerializer(videos, many=True) # 쿼리셋이 2개 이상일때

    return Response(serializer.data)
  # - POST: 새로운 비디오 생성
  # def post(self, request)
  # - DELETE, PUT; X


# -VideoDetail
#   api/v1/videos/{video_id}
class VideoDetail(APIView):
  def get_object(self, pk):
    # return get_object_or-404(Video, pk=pk)
    try:
      return Video.objects.get(pk=pk)
    except Video.DoesNotExist:
      raise NotFound
    
  # - GET: 특정 비디오 상제 조회  
  def get(self, request, pk): # pk: primary key(ID)
    # video = Video.objects.get(pk)
    video = Video.get_object(pk)
    serializer = VideoSerializer(video)

    return Response(serializer.data)
  # - POST: X
  # - PUT: 특정 비디오 정보 업데이트(수정)
  # def put(self, request, video_id):
  # - DELETE: 특정 비디오 삭제
  # def delete(self, request, video_id):