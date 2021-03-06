from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from PontoTuristico.models import PontoTuristico

class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('id','nome','descricao')
        # fields = ('id','nome','descricao','provado','tracoes','comentarios','valiacoes','endereco')
