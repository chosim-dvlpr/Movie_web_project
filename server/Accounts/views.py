from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer, UserIdSerializer
from rest_framework.permissions import AllowAny

from .models import User
from django.shortcuts import get_object_or_404

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    # 아이디, 비번, 비번 확인
    password = request.data.get('password') 
    password_confirm = request.data.get('passwordConfirm') 

    if password != password_confirm: # password_confirm != password 아닌가?
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(data=request.data)
    # 유효성 검사
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def login(request):
    if request.method == 'GET':
        info = get_object_or_404(User)
        serializer = UserIdSerializer(info)
        return Response({
            'userId': serializer.data['id'],
            'username': serializer.data['username'],
        })