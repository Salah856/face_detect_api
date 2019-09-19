# The future is now!
import uuid

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
import os

from django.conf import settings


class Image(APIView):

    def post(self, request, *args, **kwargs):

        img = request.FILES['image']
        img_extension = os.path.splitext(img.name)[-1]
        default_storage.save(settings.MEDIA_URL+str(uuid.uuid4()) + img_extension, img)

        return Response({"success":"accepted"}, status=status.HTTP_202_ACCEPTED)
