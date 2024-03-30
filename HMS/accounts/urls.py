from django.urls import path
from .views import UserRegistration
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user_registration'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]