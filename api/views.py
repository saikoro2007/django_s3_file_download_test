import boto3
from django.http import HttpResponse
from rest_framework.views import APIView


class FileView(APIView):

    def get(self, request):
        s3 = boto3.resource('s3')
        BUCKET_NAME = 'test-qiita'
        FILE_NAME = 'test.txt'
        object = s3.Object(BUCKET_NAME, FILE_NAME).get()
        response = HttpResponse(object['Body'].iter_chunks(), content_type=object['ContentType'])
        response['Content-Disposition'] = f'attachment; filename="{FILE_NAME}"'

        return response
