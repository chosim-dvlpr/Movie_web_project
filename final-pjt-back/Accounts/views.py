from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer, UserIdSerializer
from rest_framework.permissions import AllowAny
from django.http.response import JsonResponse

from django.contrib.auth import get_user_model
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
    print(request.data)
    serializer = UserSerializer(data=request.data)
    # 유효성 검사
    if serializer.is_valid(raise_exception=True):
        print('***************************************************************')
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer)

@api_view(['GET'])
def login(request):
    if request.method == 'GET':
        user = request.user
        info = get_object_or_404(User, id=user.id)
        print('실행')
        serializer = UserIdSerializer(info)
        return Response({
            'userId': serializer.data['id'],
            'username': serializer.data['username'],
        })

# @api_view(['GET'])
# def login(request):
#     if request.method == 'GET':
#         user = request.user
#         try:
#             info = User.objects.get(id=user.id)
#         except User.DoesNotExist:
#             return Response({'error': '사용자를 찾을 수 없습니다.'}, status=404)

#         print('실행')
#         serializer = UserIdSerializer(info)  # UserIdSerializer를 User에 맞게 변경해야 함
#         return Response({
#             'userId': serializer.data['id'],
#             'username': serializer.data['username'],
        # })

@api_view(['POST'])
def follow(request, username):
    if request.method == 'POST':
        if request.user.is_authenticated:
            User = get_user_model()
            me = request.user
            you = User.objects.get(username=username)
            if me != you:
                if you.followers.filter(pk=me.pk).exists():
                    you.followers.remove(me)
                    is_followed = False # 팔로우 여부 저장
                else:
                    you.followers.add(me)
                    is_followed = True
                context = {
                    'is_followed': is_followed,
                    'followers_count': you.followers.count(),
                    'followings_count': you.followings.count(),
                }
                return JsonResponse(context)
      