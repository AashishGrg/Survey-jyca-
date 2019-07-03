from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = {
            "msg": "Successfully Logged Out",
        }
        try:
            user = request.user
            print(user)
            tokens = Token.objects.filter(user=request.user)
            if len(tokens) != 0:
                for token in tokens:
                    token.delete()

                return Response(data=data, status=status.HTTP_200_OK)
            else:
                return Response(data="USER_NOT_FOUND", status=status.HTTP_400_BAD_REQUEST)
        except KeyError as error:
            print(error)
            return Response(data="USER_NOT_FOUND", status=status.HTTP_400_BAD_REQUEST)
