from . import views
from django.urls import path

urlpatterns = [
     path('',views.PostList.as_view(), name='post_detail'),
     path('<slug:slug>/',views.PostList.as_view(), name='post_detail'),
]
