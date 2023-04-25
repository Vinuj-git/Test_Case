from django.db import router
from django.urls import path,include
#from rest_framework import routers
from Test.views import RegisterApiView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)
from  Test import views
#router=routers.DefaultRouter()
# router.register('user',RegiterApiView)
urlpatterns = [
   
    #path('',include(router.urls)),
    # path('like_add/',views.like_add.as_view(),name='like_add'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/',RegisterApiView.as_view()),
    path('api/posts', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view())

]
