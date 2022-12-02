from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from users.views import UserViewSet, LoginAPIView

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='api_token_auth'),
]

urlpatterns += router.urls
