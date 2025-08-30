from rest_framework import serializers
from funcoes.models import Funcao


class FuncaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Funcao
        fields = '__all__'
