# Instead of using vanilla django views, use DRF views for our API
from rest_framework import generics
from .serializers import ReadingListSerializer
from .models import Readinglist
from .permissions import IsOwnerOrReadOnly


# have a list view
class ReadinglistList(generics.ListCreateAPIView):
    queryset = Readinglist.objects.all()  # gets all the Reading lists
    serializer_class = ReadingListSerializer


# have a detail view
class ReadinglistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly,]
    queryset = Readinglist.objects.all()  # gets all the Reading lists
    serializer_class = ReadingListSerializer
