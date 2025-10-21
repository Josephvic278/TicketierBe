from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer, DeviceSerializer
from .models import Device
from rest_framework.views import APIView


class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


class MeView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class DeviceRegisterView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = DeviceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        device, _ = Device.objects.update_or_create(
            device_token=serializer.validated_data['device_token'],
            defaults={'name': serializer.validated_data.get('name', ''), 'last_seen_at': serializer.validated_data.get('last_seen_at')},
        )
        return Response(DeviceSerializer(device).data, status=status.HTTP_201_CREATED)
