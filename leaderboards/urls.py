from django.conf.urls import include, patterns, url
from rest_framework import routers
from leaderboards import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users?', views.UserViewSet)
router.register(r'games?', views.GameViewSet)
router.register(r'speedruns?', views.SpeedrunViewSet)
router.register(r'platforms?', views.PlatformViewSet)

urlpatterns = patterns(
    '',
    url(r'^api/login(?:\.(?P<format>[a-z0-9]+))?$', views.LoginViewSet.as_view()),
    url(r'^api/logout(?:\.(?P<format>[a-z0-9]+))?$', views.LogoutViewSet.as_view()),
    url(r'^api/', include(router.urls)),
)
