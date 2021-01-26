from django.db import models


"""
    Criação dos modelos da aplicação com base na diagramação.
"""


class Time(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    team = models.CharField(max_length=70)
    noc = models.CharField(max_length=20)

    def __str__(self):
        return self.team


class Evento(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    games = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    season = models.CharField(max_length=100)
    city = models.CharField(max_length=70)
    sport = models.CharField(max_length=50)
    event = models.CharField(max_length=100)

    def __str__(self):
        return self.event


class Medalha(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    desc = models.CharField(max_length=20)

    def __str__(self):
        return self.desc


class Pessoa(models.Model):
    id = models.IntegerField(primary_key=True, blank=False)
    id_evento = models.ManyToManyField(Evento)  # , related_name='event'
    id_medalha = models.ManyToManyField(Medalha)  # , related_name='medal'
    id_time = models.ManyToManyField(Time)  # , related_name='team'
    name = models.CharField(max_length=70)
    sex = models.CharField(max_length=15)
    age = models.CharField(max_length=7)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
