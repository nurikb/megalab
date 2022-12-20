from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import RegistrationAPIView, LoginAPIView, UserAPIView

router = DefaultRouter()

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view(), name='api_token_auth'),
    path('login/', LoginAPIView.as_view(), name='api_token_auth'),
    path('user/', UserAPIView.as_view(), name='user')
]
urlpatterns += router.urls
