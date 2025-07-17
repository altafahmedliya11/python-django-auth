# from .serializers import UserSerializer
from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


# ViewSets define the view behavior.
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def create(self, request):
        try:
            print("Here i am")
            user = User.objects.create_user(
                request.data["username"],
                request.data["first_name"],
                request.data["last_name"],
                request.data["email"],
                request.data["password"],
            )
            return Response(
                {
                    "success": True,
                    "message": "User created successfully",
                    "status_code": 201,
                    "data": UserSerializer(user, context={"request": request}).data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
