from rest_framework import serializers
from tiposriscos.models import TipoRisco


class TipoRiscoSerializer(serializers.ModelSerializer):

    class eta:
        model = TipoRisco
        fields = '__all__'