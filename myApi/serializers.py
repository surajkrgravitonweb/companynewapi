from rest_framework import serializers
from .models import Form1,Form2

class Form1Serializers(serializers.ModelSerializer):
    class Meta:
        model=Form1
        fields='__all__'


class Form2Serializers(serializers.ModelSerializer):
    class Meta:
        model=Form2
        fields='__all__'


class Form3Serializers(serializers.ModelSerializer):
    class Meta:
        model=Form2
        fields='__all__'