from django.urls import path
from .. import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('',views.getRoutes),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh',TokenRefreshView.as_view(), name='token_obtain_pair'),
    path('register/', views.UserRegisterView.as_view(), name='auth_register')
]