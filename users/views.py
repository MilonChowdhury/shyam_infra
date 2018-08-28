from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets,status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from users.serializers import *
from django.contrib.auth.models import Permission


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        print('user:', user)
        serializer = UserLoginSerializer(user, many=True)

        if user:
            # user_groups=list()
            user_group = user.groups.all()
            for item in user_group:
                user_group = item.name
            perm_tuple = [{'id': x.id, 'name': x.name} for x in Permission.objects.filter(user=user)]

            return Response({
                'token': token.key,
                'user_id': user.pk,
                'username': user.username,
                'email': user.email,
                'user_type': user_group,
                'group_permissions': user.get_group_permissions(),
                'user_permissions': perm_tuple,

            })
        else:
            return Response({'message': 'Invalid Login', 'status': status.HTTP_400_BAD_REQUEST})

