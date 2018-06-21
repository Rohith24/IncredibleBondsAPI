from django.views.generic import CreateView
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import generics, permissions
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import *

from IncredibleBonds.models import *
from IncredibleBonds.serializers import *

@api_view(['POST'])
@permission_classes((AllowAny,))
def create_user(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class PatientsViewSet(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer



class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Profile.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FactorManufactureViewSet(viewsets.ModelViewSet):
    queryset = FactorManufacture.objects.all()
    serializer_class = FactorManufactureSerializer


class Patients(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class HemophiliaList(viewsets.ModelViewSet):
    queryset = Hemophilia.objects.all()
    serializer_class = HemophiliaSerializer


class InfusionLogList(viewsets.ModelViewSet):
    queryset = InfusionLog.objects.all()
    serializer_class = InfusionLogSerializer


class Register(APIView):

    # def get(self, request):
    #     return Response(RegisterSerializer().data, status=status.HTTP_200_OK)
    #
    # def post(self, request):
    #     if request.user.is_authenticated:
    #         serializer = RegisterSerializer(data=request.user)
    #         if serializer.is_valid():
    #             return Response(serializer.data, status=status.HTTP_302_FOUND)
    #     serializer = RegisterSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user = serializer.save()
    #         if user:
    #             print(serializer.data)
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)

    pass