import requests
import json
import os

#crud da api firebase

# usar link da api da firebase
#meu link está setado como secreto
#modificar para o link do seu projeto firebase banco de dados em tempo real.

link = os.environ['LINK']

#inserir dados do produto no banco
#pode ser inserido outros dados
def cadastrar():
	nome=input("digite o nome:")
	preco=input("digite o preço:")
	quant=input("digite a quantidade:")
	#dados formatados a serem inseridos
	dados ={f'nome': nome,'preco': preco,'quantidade':quant}
	#inserindo dados no firebase por meio de requisição post. 
	#json.dumps transforma em json o dicionário.
	requisicao = requests.post(f'{link}/produto/.json',data=json.dumps(dados))
	
	print(requisicao)
	#mostra o id do produto cadastrado
	print(requisicao.text)

#get de tudo do banco
def pesquisar():
	print("digite qual registro deseja pesquisar")
	opcao = input("")
	requisicao = requests.get(f"{link}/produto/{opcao}/.json")
	#mostra o código do request
	#mostra o que tem na requisição
	txt = requisicao.text
	#transforma requisição em dicionário python
	dic=json.loads(txt)
	nome = dic['nome']
	preco = dic['preco']
	quantidade = dic['quantidade']
	req_txt = f"nome:{nome} preço:{preco} quantidade:{quantidade}"
	print(req_txt)
#atualizar registro por id	
def update():
	nome=input("digite o nome:")
	preco=input("digite o preço:")
	quant=input("digite a quantidade:")
	dados ={f'nome': nome,'preco': preco,'quantidade':quant}
	print("qual registro deseja deletar/n")
	opcao = input("")
	requisicao = requests.patch(f'{link}/produto/{opcao}/.json',data=json.dumps(dados))
	
	print(requisicao)
	print(requisicao.text)
	
#deletar o registro pela chave
def deletar():
	requisicao = requests.get(f"{link}.json")
	#mostra o código do request
	print(requisicao)
	print("")
	#transforma requisição em dicionário python
	dic = requisicao.json()
	#escolher apenas uma parte do dicionario
	#mostra as chaves que podem ser deletadas
	print(dic['produto'].keys())
	
	#escolha de registro
	print("qual registro deseja deletar/n")
	opcao = input("")
	#requisição para deletar
	requisicao = requests.delete(f'{link}/produto/{opcao}/.json')
	print(requisicao)
	print(requisicao.text)

#início da escolha
print("o que deseja fazer")
opcao = input("1-cadastrar 2-pesquisar 3-deletar 4-atualizar")
if opcao == "1":	
	cadastrar()
elif opcao == "2":
	pesquisar()
elif opcao == "3":
	deletar()
elif opcao == "4":
	update()
else:
	print("erro")