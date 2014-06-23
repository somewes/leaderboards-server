from __future__ import unicode_literals
from django.contrib.auth.models import User
from rest_framework import viewsets
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
    API endpoint that allows platforms to be viewed or edited.
    """
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
