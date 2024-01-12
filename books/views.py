# Instead of using vanilla django views, use DRF views for our API
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from .permissions import IsOwnerOrReadOnly


# have a list view
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()  # gets all the Things
    serializer_class = BookSerializer


# have a detail view
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly,]
    queryset = Book.objects.all()  # gets all the Things
    serializer_class = BookSerializer
