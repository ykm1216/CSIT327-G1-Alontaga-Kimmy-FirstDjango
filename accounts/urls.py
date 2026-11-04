from django.urls import path
from .views import DashboardLoginView, ProfileView, SignUpView

urlpatterns = [
    path('login/', DashboardLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
]