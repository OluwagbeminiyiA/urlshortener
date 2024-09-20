import json

from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.views import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_302_FOUND
from .models import URL
from .serializers import UrlSerializer
from sqids import Sqids
import uuid

sqids = Sqids('FxnXM1kBN6cuhsAvjW3Co7l2RePyY8DwaU04Tzt9fHQrqSVKdpimLGIJOgb5ZE', min_length=6)


class UrlShortenView(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = UrlSerializer

    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        long_url = request.data.get('url')
        check_url = URL.objects.filter(url=long_url).first()
        if check_url:
            return Response(data={'url': check_url.short_url})
        instance = serializer.save()
        unique_number = instance.id
        print(unique_number)
        key = sqids.encode([int(instance.id)])
        url = f'http://127.0.0.1:8000/{key}'
        serializer.save(key=key, short_url=url)
        headers = self.get_success_headers(serializer.data)
        return Response(data={'key': key, 'short_url': url}, headers=headers)


class UrlRedirectView(viewsets.ViewSet):
    lookup_field = 'key'
    http_method_names = ['get']
    serializer_class = UrlSerializer

    def retrieve(self, request, key=None):
        key = key
        original_url = URL.objects.filter(key=key).first()

        if not original_url:
            return Response(data={'Error 404': 'URL not found'}, status=HTTP_404_NOT_FOUND)

        return redirect(original_url.url)
        # return Response(data={'location': original_url.url}, status=HTTP_302_FOUND)
