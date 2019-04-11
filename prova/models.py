from django.db import models

# Create your models here.


class Resposta(models.Model):
    conteudo = models.CharField(max_length=250)
    id_questao = models.ForeignKey('Questao', on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.id_questao)+' - '+ self.conteudo)


class Questao(models.Model):
    nome = models.CharField(max_length=50)
    enunciado = models.TextField()
    resposta_correta = models.OneToOneField(Resposta, null=True, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.nome

# NameError: name 'Questao' is not defined
