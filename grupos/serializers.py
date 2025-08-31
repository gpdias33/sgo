from rest_framework import serializers
from grupos.models import Grupo


class GrupoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grupo
        fields = '__all__'
