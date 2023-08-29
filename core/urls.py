from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve 
from django.urls import re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/affiliate/', include('user.urls')),
    path('v1/', include('post.urls')),
    path('v1/login/', TokenObtainPairView.as_view()),
    path('v1/refresh/', TokenRefreshView.as_view()),
    path('v1/verify/', TokenVerifyView.as_view()),
    path('',views.apiMsg)
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
