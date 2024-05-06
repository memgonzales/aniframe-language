from rest_framework import serializers

from .models import Codes


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codes
        fields = ("id", "code")
        # , 'filename'
