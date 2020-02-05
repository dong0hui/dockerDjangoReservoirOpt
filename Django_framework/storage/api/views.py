from ..models import BlobBlockService
from . import serializers

from rest_framework import generics, status
from rest_framework.response import Response

class StorageDownloadView(generics.CreateAPIView):
    """Create a record in databse
    Download the job data from blob to container
    """
    queryset = BlobBlockService.objects.all()
    serializer_class = serializers.BlobBlockServiceSerializer

    def download(self, request, *args, **kwargs):
        super(StorageDownloadView, self).download(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Request written to database",
                    "userInfo": request.data}
        return Response(response)
