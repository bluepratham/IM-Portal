from rest_framework import serializers
from .models import IronMan


class IronManSerializer(serializers.ModelSerializer):

    class Meta:
        model = IronMan
        fields = "__all__"
