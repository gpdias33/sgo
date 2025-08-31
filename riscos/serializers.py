from rest_framework import serializers
from riscos.models import Risco


class RiscoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Risco
        fields = '__all__'
