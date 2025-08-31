from rest_framework import serializers
from tiposexames.models import TipoExame


class TipoExameSerializer(serializers.ModelSerializer):

    class eta:
        model = TipoExame
        fields = '__all__'