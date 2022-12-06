from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import RegistrationViewSet, LoginAPIView

router = DefaultRouter()
router.register('registration', RegistrationViewSet)


urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='api_token_auth'),
]
urlpatterns += router.urls
