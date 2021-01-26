#from .models import Time, Pessoa, Evento, Medalha
from .models import Evento, Time, Medalha, Pessoa
from django.conf import settings
import csv


# "ID","Name","Sex","Age","Height","Weight"


def adicionar_pessoa(reader):
    for row in reader:
        try:  # se já tem mas com evento diferente então adiciona
            obj = Pessoa.objects.filter(team=row['Team'], noc=row['NOC']).get()
            print(obj.id_evento)
            continue
        except:
            pass

        Pessoa.objects.create(team=row['Team'], noc=row['NOC'])


def adicionar_time(reader):
    for row in reader:
        try:
            Time.objects.filter(team=row['Team'], noc=row['NOC'])
            continue
        except:
            pass

        Time.objects.create(team=row['Team'], noc=row['NOC'])


def adicionar_medalha(reader):
    for row in reader:
        try:
            Medalha.objects.filter(desc=row['Medal'])
            continue
        except:
            pass

        Medalha.objects.create(desc=row['Medal'])


def adicionar_eventos(reader):
    print('passou aqui')
    for row in reader:

        try:
            Evento.objects.filter(games=row['Games'], year=row['Year'], season=row['Season'], city=row['City'],
                                  sport=row['Sport'], event=row['Event'])
            continue
        except:
            pass
        print('passou aqui2')
        Evento.objects.create(row['Games'], row['Year'], row['Season'], row['City'], row['Sport'], row['Event'])


with open('../desafio_celero/athlete_events.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader)
    # separa a pessoa e vincula ela a um evento diferente
    # o id é da pessoa, cadastrar 1 eventos e medalhas e times

    adicionar_eventos(reader)
    adicionar_medalha(reader)
    adicionar_time(reader)
