from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Data
from .serializer import DatasSerializer,DataSerializer, DataTrainSerializer,DataPredictSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from .helpers import train, predict

class DatasAPIView(APIView):

    def get(self, request):
        Datas = Data.objects.all()
        serializer = DatasSerializer(Datas,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DatasSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class DataAPIView(APIView):


    def get(self, request, pk):
        data = Data.objects.filter(id=pk)
        serializer = DataSerializer(data, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        data = Data.objects.get(id=pk)
        serializer = DataSerializer(data, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request):
        data = Data.objects.get(id=request.data.get('data_id'))
        data.delete()
        return Response(status=200)

class DataTrainAPI(APIView):

    def post(self, request):
        Datas = Data.objects.all()
        serializer = DataTrainSerializer(Datas,many=True)
        train()
        return Response(serializer.data)

class DataPredictAPI(APIView):

    def post(self, request):
        text = request.data.get("text")
        if text != "":
            data = predict(text)
            serializer = DataPredictSerializer(data=data).initial_data
            return Response(serializer)

