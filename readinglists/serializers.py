# Serializers change the django models into JSON
from rest_framework import serializers
# The model we are serializing (representing as JSON)
from .models import Readinglist


class ReadingListSerializer(serializers.ModelSerializer):
    # Defines an inner class, Meta, which is used to specify metadata about the serializer class.
    class Meta:
        # a tuple of strings, representing all the strings we want to serialize
        fields = ("id", "owner", "books")
        # the model to serialize
        model = Readinglist
