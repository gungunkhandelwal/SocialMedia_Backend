from rest_framework.response import Response
from rest_framework.views import APIView
from . serializers import *
from rest_framework import status
from django.contrib.auth import authenticate,logout
from rest_framework.authtoken.models import Token

class RegisterView(APIView):
    def post(self,request):
        data=request.data
        print(data)
        serializer=RegisterSerializer(data=data)
        if not serializer.is_valid():
            return Response(
                {
                    'status':False,
                    'message':serializer.errors,
                },status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return Response({'status':True,'message':'User Created'},status.HTTP_200_OK)
    

class LoginView(APIView):
    def post(self,request):
        data=request.data
        print(data)
        serializer=LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response(
                {
                    'status':False,
                    'message':serializer.errors,
                },status.HTTP_400_BAD_REQUEST
            )
        user=authenticate(username=serializer.data['username'],password=serializer.data['password'])
        print(user)
        if user is None:
            return Response(
                {
                    'status': False,
                    'message': 'Invalid username or password',
                }, status=status.HTTP_401_UNAUTHORIZED
            )
        token, created = Token.objects.get_or_create(user=user)
        
        return Response(
            {
                'status': True,
                'message': 'User logged in',
                'token':str(token),
            }, status=status.HTTP_200_OK
        )
    
class LogoutView(APIView):
    def post(self,request):
        logout(request)
        return Response(
            {
                'status': True,
                'message': 'User logged out'
            }, status=status.HTTP_200_OK
        )
