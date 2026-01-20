from django.contrib.auth.models import User
from rest_framework import  viewsets, permissions,generics
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer,EmailTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
# Create your views here.
   
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    
class LoginView(TokenObtainPairView):
    serializer_class = EmailTokenSerializer

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self,request):
        try:
            refresh = request.data.get("refresh")
            token = RefreshToken(refresh)
            token.blacklist()
            return Response({"message":"Logged out successfully"})          
        except Exception:
            return Response({"message":"Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
            
        