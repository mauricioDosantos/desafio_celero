API rest - Desafio Celero
==============

Esta API tem a finalidade de servir os dados do dataset "120 years of Olympc history: athletes and results" obtido no Kaggle. Funcionalidades de adicionar, alterar, atualizar e deletar dados.

## dependências
*Python 3.8.5
*Django 3.1.5
*Django rest framework 3.12.2

## modo de uso
Esta API pode ser acessa pelo comando curl, caso seu sistema não tenha poderá baixa-lo fácilmente na web

*CURL

Para consultar uma linha utilize o método GET, da seguinte forma:
	curl -X GET http://localhost:8000/api/v1/PessoaList/<id>

Para adicionar os dados utilize o método POST

	curl -d "@teste.json" -H "Content-Type:application/json" -X POST http://localhost:8000/api/v1/PessoaList/

estrutua do JSON para método POST, exemplo:

	{"id": 4,
 "name": "clenpfs",
 "sex": "feminino",
 "age": "19",
 "height": "1.70",
 "weight": "70.0",
 "id_time": [
            1
        ],
 "id_evento": [
            1
        ],
 "id_medalha": [
            1
        ]
}

Para atualizar os dados de alguma linha utilize o método PUT

	curl -d "@teste.json" -H "Content-Type:application/json" -X PUT http://localhost:8000/api/v1/PessoaList/<id>

estrutua do JSON para método POST, exemplo:

	{"id": 4,
 "name": "clenpfs",
 "sex": "feminino",
 "age": "19",
 "height": "1.70",
 "weight": "70.0",
 "id_time": [
            1
        ],
 "id_evento": [
            1
        ],
 "id_medalha": [
            1
        ]
}

Para deletar alguma linha utilize o comando:
	curl -X DELETE http://localhost:8000/api/v1/PessoaList/<id>
