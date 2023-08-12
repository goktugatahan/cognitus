from django.urls import path, include
from .views import DatasAPIView, DataAPIView, DataTrainAPI,DataPredictAPI

urlpatterns = [
    path('', DatasAPIView.as_view(),name="get_datas"),
    path('data/<int:pk>/', DataAPIView.as_view(),name="get_data"),
    path('data/delete/', DataAPIView.as_view(),name="delete_data"),
    path('data/train/', DataTrainAPI.as_view(),name="train_data"),
    path('data/predict/', DataPredictAPI.as_view(),name="predict_data")
]