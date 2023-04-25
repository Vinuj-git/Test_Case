from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from .serializer import UserSerializer,PostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from Test.permissions import IsOwnerOrReadOnly

from .models import *

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterApiView(APIView):
    serializer_class = UserSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user= serializer.save()
            resfresh = RefreshToken.for_user(user)
            response_data = {'refresh':str(resfresh),'access':str(resfresh.access_token)}
            # serializer_data = serializer.data
            return Response(response_data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    

    @api_view(['POST'])
    def update_Post(request, pk):
        item = Post.objects.get(pk=pk)
        data = PostSerializer(instance=item, data=request.data)
 
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        try:
            if request.user==True:
                # do your customization here
                user_object = self.get_object()
                Post.objects.filter(id=user_object.id).delete()
                user_object.delete()
                response={
                    "msg":"Post deleted successfully",
                    "status":True
                }
                return Response(response,status=status.HTTP_204_NO_CONTENT)
            else:
                response = {
                        'status': False,
                        'code': status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                        'msg': "NON_AUTHORITATIVE",
                    }  
                return Response(response,status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        except :
            return Response (status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]