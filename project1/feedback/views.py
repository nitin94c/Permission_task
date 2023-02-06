# from rest_framework import viewsets
# from .serializers import FeedBackSerializer
# from .models import FeedBack
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAdminUser
# from .permissions import IsOwnerOrReadOnly

# class FeedbackViewSet(viewsets.ModelViewSet):
#     serializer_class = FeedBackSerializer
#     queryset = FeedBack.objects.all()
#     # authentication_classes = [JWTAuthentication]
#     # permission_classes = [IsOwnerOrReadOnly]


from rest_framework.response import Response
from .models import FeedBack
from .serializers import FeedBackSerializer
from rest_framework.generics import ListAPIView,CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwnerOrReadOnly

class FeedbackCreateApi(CreateAPIView):
    serializer_class = FeedBackSerializer
    queryset = FeedBack.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class FeedbackShowApi(ListAPIView):
    serializer_class = FeedBackSerializer
    queryset = FeedBack.objects.all()
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]


class FeedbackUpdateApi(RetrieveUpdateDestroyAPIView):
    serializer_class = FeedBackSerializer
    queryset = FeedBack.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication]







    
