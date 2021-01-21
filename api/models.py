from django.db import models


"""
    Criação dos modelos da aplicação com base na diagramação.
"""


class Pessoa(models.Model):
    id = models.IntegerField(primary_key=True, blank=False)
    name = models.CharField(max_length=70)
    sex = models.CharField(max_length=15)
    age = models.CharField(max_length=7)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)


    

class Time(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    team = models.CharField(max_length=70)
    noc = models.CharField(max_length=20)
    

class Evento(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    games = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    season = models.CharField(max_length=100)
    city = models.CharField(max_length=70)
    sport = models.CharField(max_length=50)
    event = models.CharField(max_length=100)


class Medalha(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    desc = models.CharField(max_length=20)
    

class PessoaTime(models.Model):
    id_pessoa_fk = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    id_time_fk = models.ForeignKey(Time, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['id_pessoa_fk', 'id_time_fk']


class MedalhaPessoa(models.Model):
    id_pessoa_fk = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    id_medalha_fk = models.ForeignKey(Medalha, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['id_pessoa_fk', 'id_medalha_fk']


class PessoaEvento(models.Model):
    id_pessoa_fk = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    id_evento_fk = models.ForeignKey(Evento, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['id_pessoa_fk', 'id_evento_fk']
