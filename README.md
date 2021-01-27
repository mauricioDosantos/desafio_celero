API rest - Desafio Celero
==============

Esta API tem a finalidade de servir os dados do dataset "120 years of Olympc history: athletes and results" obtido no Kaggle. Funcionalidades de adicionar, alterar, atualizar e deletar dados.

## dependências
● Python 3.8.5
● Django 3.1.5
● Django rest framework 3.12.2

## modo de uso
Esta API pode ser acessada por meio de requisições GET, POST, PUT, DELETE, com envio de JSON.
Segue exemplo utilizando o comando curl, caso seu sistema operacional não tenha, poderá baixa-lo fácilmente na web.

● CURL

Os comandos devem ser utilizados para as seguintes urls, com seus respectivos métodos:
	
	/api/v1/PessoaList/<id>   -> GET, PUT, DELETE
	/api/v1/PessoaList/   -> POST
	
	/api/v1/TimeList/<id>   -> GET, PUT, DELETE
	/api/v1/PessoaList/   -> POST
	
	/api/v1/MedalhaList/<id>   -> GET, PUT, DELETE
	/api/v1/PessoaList/   -> POST
	
	/api/v1/EventoList/<id>   -> GET, PUT, DELETE
	/api/v1/PessoaList/   -> POST

Para consultar uma linha utilize o método GET, da seguinte forma:

	curl -X GET http://api-celero.herokuapp.com/api/v1/PessoaList/<id>

Para adicionar os dados utilize o método POST

	curl -d "@teste.json" -H "Content-Type:application/json" -X POST http://api-celero.herokuapp.com/api/v1/PessoaList/

estrutura do JSON para método POST, exemplo:

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

	curl -d "@teste.json" -H "Content-Type:application/json" -X PUT http://api-celero.herokuapp.com/api/v1/PessoaList/<id>

Estrutua do JSON para método PUT, exemplo:

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

	curl -X DELETE http://api-celero.herokuapp.com/api/v1/PessoaList/<id>
