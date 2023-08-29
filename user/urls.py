from django.urls import path
from user.views import LoginView, ProviderCreate, BlacklistRefreshView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('provider/signup/', ProviderCreate.as_view()),
    path('logout/', BlacklistRefreshView.as_view()),
]

