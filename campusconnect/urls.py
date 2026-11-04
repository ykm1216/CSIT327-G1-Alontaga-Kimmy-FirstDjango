from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from dashboard.views import AdminPanelView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin-panel/', AdminPanelView.as_view(), name='admin_panel'),
    path('dashboard/', include('dashboard.urls')),
]