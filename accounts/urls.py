from django.urls import path
from .views import DashboardLoginView, SignUpView

urlpatterns = [
    path('login/', DashboardLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
]