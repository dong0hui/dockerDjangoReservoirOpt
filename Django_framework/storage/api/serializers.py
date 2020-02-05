from ..models import BlobBlockService
from rest_framework import serializers

class BlobBlockServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlobBlockService
        fields = ('username', 'blobaccount', 'blobcontainer')