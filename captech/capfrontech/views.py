from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = employees.objects.all()
    serializer_class = employee_hireSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new employees."""
        serializer.save()



class CreateViews(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Titles.objects.all()
    serializer_class = titlesSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new employees."""


        serializer.save()

class Createviews(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Salaries.objects.all()
    serializer_class = salariesSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new employees."""
        serializer.save()