from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from IncredibleBondsAPI import settings

from IncredibleBonds.models import FactorManufacture, Hemophilia, Patient, Parent, Doctor, InfusionLog, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_Number', 'password', 'is_patient', 'is_parent', 'is_doctor')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class FactorManufactureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FactorManufacture
        fields = "__all__"


class HemophiliaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hemophilia
        fields = "__all__"


class InfusionLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InfusionLog
        fields = "__all__"


# class RegisterSerializer(serializers.ModelSerializer):
#
#     email = serializers.EmailField(
#         required=True,
#         validators=[UniqueValidator(queryset=settings.AUTH_USER_MODEL.objects.all())]
#     )
#     username = serializers.CharField(
#         validators=[UniqueValidator(queryset=settings.AUTH_USER_MODEL.objects.all())]
#     )
#     password = serializers.CharField(min_length=8)
#
#     def create(self, validated_data):
#         user = settings.AUTH_USER_MODEL.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
#         return user
#
#     class Meta:
#         model = settings.AUTH_USER_MODEL
#         fields = ('id', 'username', 'email', 'password')
#
# #          'is_patient', 'is_doctor','is_patient','is_parent','gender','blood_group',
# #                            'phone_Number','state','district','city'
