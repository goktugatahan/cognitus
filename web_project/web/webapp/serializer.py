from rest_framework import serializers
from .models import Data

class DatasSerializer(serializers.Serializer):
    text = serializers.CharField()
    label = serializers.CharField()

    def validate_label(self, label):
        if label is None:
            raise serializers.ValidationError("Label is None")
        return label

    def validate_label(self, text):
        if text is None:
            raise serializers.ValidationError("Text is None")
        return text

    class Meta:
        model = Data
        fields = ('id','text','label')

class DataSerializer(serializers.Serializer):

    text = serializers.CharField()
    label = serializers.CharField()

    def validate_label(self, label):
        if label is None:
            raise serializers.ValidationError("Label is None")
        return label

    def validate_label(self, text):
        if text is None:
            raise serializers.ValidationError("Text is None")
        return text

    class Meta:
        model = Data
        fields = ('id','text','label')

class DataTrainSerializer(serializers.Serializer):

    text = serializers.CharField()
    label = serializers.CharField()

    def validate_label(self, label):
        if label is None:
            raise serializers.ValidationError("Label is None")
        return label

    def validate_label(self, text):
        if text is None:
            raise serializers.ValidationError("Text is None")
        return text

    class Meta:
        model = Data
        fields = ('id','text','label')

class DataPredictSerializer(serializers.Serializer):

    text = serializers.CharField()
    label = serializers.CharField()

    def validate_label(self, label):
        if label is None:
            raise serializers.ValidationError("Label is None")
        return label

    def validate_label(self, text):
        if text is None:
            raise serializers.ValidationError("Text is None")
        return text

    class Meta:
        model = Data
        fields = ('text','label')