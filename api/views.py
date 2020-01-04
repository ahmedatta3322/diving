from divers.models import Divers , Courses
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from api.serializer import DiverSerializer , CourseSerializer
from rest_framework import authentication, permissions,routers,generics
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.parsers import FormParser,MultiPartParser,JSONParser,FileUploadParser
from rest_framework import status

class divers(generics.ListCreateAPIView):
    
    parser_classes = [MultiPartParser,FormParser]
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = Divers.objects.all()
    serializer_class = DiverSerializer
    def post(self, request):
        serialzer = self.get_serializer(data = request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        else:
            print('error1', serialzer.errors)
            print(request.data)
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        print(request.data)
class courses(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser,FormParser]
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer 
    def post(self , request):
        serialzer = self.get_serializer(data = request.data)
        if serialzer.is_valid():
            serialzer.save()
            print(request.data)
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        else:
            print('error1', serialzer.errors)
            print(request.data)
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        print(request.data)



