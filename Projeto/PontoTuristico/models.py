from django.db import models
from Atracoes.models import Atracao
from Comentarios.models import Comentario
from Avaliacoes.models import Avaliacao
from Localizacoes.models import Localizacao
# Create your models here.
class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao) #um ponto turistico pode ter muitas ataçoes ManyToMany
    comentarios = models.ManyToManyField(Comentario)
    Avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Localizacao,on_delete=models.CASCADE)

    def __str__(self) :
        return self.nome