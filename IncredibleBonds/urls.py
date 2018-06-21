from django.urls import include, path

from . import views
from accounts.views import CustomAuthToken

urlpatterns = [
    path('users', views.UserViewSet.as_view()),
    path('patients', views.PatientsViewSet.as_view()),
    path('register', views.create_user),
    path('login', CustomAuthToken.as_view()),
]