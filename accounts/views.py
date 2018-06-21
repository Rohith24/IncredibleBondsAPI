from django.shortcuts import redirect
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import generics, permissions
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.views import *
from rest_auth.views import django_login
from IncredibleBonds.models import *
from IncredibleBonds.serializers import *

# @api_view(['POST'])
# def login_view(request):
#     if request.user.is_authenticated():
#         return redirect("home")
#     next = request.GET.get('next')
#     title = "Login"
#     form = UserSerializer(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         request.session.set_expiry(10800)
#         django_login(request, user)
#         if next:
#             return redirect(next)
#         if user.is_staff:
#             return redirect("TeacherHome")
#         else:
#             return redirect("StudentHome")
#     return Response({"form":form, "title": title , "password_reset":True}, status=status.HTTP_200_OK)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })