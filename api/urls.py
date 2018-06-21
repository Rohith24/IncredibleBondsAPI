from django.urls import include, path

urlpatterns = [
    path('users/', include('IncredibleBonds.urls')),
    path('rest-auth/', include('rest_auth.urls')),
]