from django.urls import path
from . import views

urlpatterns = [ # api/v1/videos/
  path('', views.VideoList.as_view,name='Video-List'),
  path('<int:pk/', views.VideoDetail.as_view, name='Video-Detail'),

]