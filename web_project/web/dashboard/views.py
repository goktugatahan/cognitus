from django.shortcuts import render
from webapp.models import Data
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class DatasList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'datas/webapp.html'

    def get(self, request):
        queryset = Data.objects.all()
        return Response({'datas': queryset})
