import requests
import csv
import json


times = []
eventos = []
medalhas = []

"""
    Código imcompleto, tive alguns contratempos, mas dei o meu máximo, agradeço a oportunidade. abraços Mauricio.

"""

# pegar todos os itens existentes de time, evento, medalha pois adificuldade era saber o id de cada um desses.
# esta função pega todas as linhas do banco de dados
def atualizar_listas():
    count = 1
    resT = requests.get(f'http://api-celero.herokuapp.com/api/v1/TimeList/{count}')
    while resT.status_code != 404:
        data = dict(resT.json())
        times.append(data)
        count += 1
        resT = requests.get(f'http://api-celero.herokuapp.com/api/v1/TimeList/{count}')

    count = 1
    resE = requests.get(f'http://api-celero.herokuapp.com/api/v1/EventoList/{count}')
    while resE.status_code != 404:
        data = dict(resE.json())
        eventos.append(data)
        count += 1
        resE = requests.get(f'http://api-celero.herokuapp.com/api/v1/EventoList/{count}')

    count = 1
    resM = requests.get(f'http://api-celero.herokuapp.com/api/v1/MedalhaList/{count}')
    while resM.status_code != 404:
        data = dict(resM.json())
        medalhas.append(data)
        count += 1
        resM = requests.get(f'http://api-celero.herokuapp.com/api/v1/MedalhaList/{count}')


# incompleta, função para enviar uma requisição POST para o servidor com os dados.
def adicionar_valore(comple_url, data):
    requisicao = requests.post(f'http://api-celero.herokuapp.com/api/v1/{comple_url}/', data=data)
    data = requisicao.status_code
    if data == 404:
        return False

    return True


# incompleta, comparar se tem esse mesmo item na lista referente, para assim pegar o id dele e vinvular à pessoa
def checar_se_tem(resp, identificador, nome):
    for dictionary in resp:
        if dictionary.get[f'{identificador}'] == nome:
            return dictionary.get['id']
    return False


# incompleta, para adicionar as pessoas
def adicionar_pessoa(reader):  # adiciona todas as pessoas
    for row in reader:
        pessoa = requests.get(f'http://api-celero.herokuapp.com/api/v1/PessoaList/{row["ID"]}')

        id_objE = checar_se_tem(eventos, 'event', row['Event'])
        if id_objE: # pode ser False caso não tenha nada ou um id

        # row['Team']
        # row['Medal']

        if pessoa.status_code == 404:
            #todo: adicionar

            #"ID","Name","Sex","Age","Height","Weight"
            adicionar_valore('PessoaList', {'id': row['ID'], 'name': row['Name'], 'sex': row['Sex'], 'age': row['Age'],
                                            'height': row['Height'], 'weight': row['Weight'], 'id_time': [],
                                            'id_evento': [], 'id_medalha': []})
        else:
            data = pessoa.json()


# principal
with open('athlete_events.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    while True:
        atualizar_listas()

    # pessoas só iria ser adicionada quando todos os times, eventos e medalhas foçem cadastrados
    adicionar_pessoa()



#                       Funções criadas antes, para tentar adicionar diretamente, sem ser preciso enviar requisições para o servidor.
# def adicionar_time(reader):
#     for row in reader:
#         try:
#             Time.objects.filter(team=row['Team'], noc=row['NOC'])
#             continue
#         except:
#             pass
#
#         Time.objects.create(team=row['Team'], noc=row['NOC'])
#
#
# def adicionar_medalha(reader):
#     for row in reader:
#         try:
#             Medalha.objects.filter(desc=row['Medal'])
#             continue
#         except:
#             pass
#
#         Medalha.objects.create(desc=row['Medal'])
#
#
# def adicionar_eventos(reader):
#     print('passou aqui')
#     for row in reader:
#
#         try:
#             Evento.objects.filter(games=row['Games'], year=row['Year'], season=row['Season'], city=row['City'],
#                                   sport=row['Sport'], event=row['Event'])
#             continue
#         except:
#             pass
#         print('passou aqui2')
#         Evento.objects.create(row['Games'], row['Year'], row['Season'], row['City'], row['Sport'], row['Event'])