from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from leaderboards.serializers import UserSerializer, GameSerializer, SpeedrunSerializer, PlatformSerializer
from leaderboards.models import Game, Speedrun, Platform


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows games to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class SpeedrunViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows speedruns to be viewed or edited.
    """
    queryset = Speedrun.objects.all()
    serializer_class = SpeedrunSerializer


class PlatformViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows speedruns to be viewed or edited.
    """
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class LoginViewSet(APIView):
    """
    API endpoint for logging in
    """
    def post(self, request, format=None):
        if 'username' in request.DATA and 'password' in request.DATA:
            username, password = (request.DATA['username'], request.DATA['password'])
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return Response(UserSerializer(user).data)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutViewSet(APIView):
    """
    API endpoint for logging out
    """
    def delete(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_200_OK)
