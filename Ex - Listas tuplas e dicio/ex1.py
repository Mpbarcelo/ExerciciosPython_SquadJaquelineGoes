# Exercício 01
perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?",
             "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

respostas_positivas = 0

for pergunta in perguntas:
    resposta = input(pergunta + " (s/n): ")
    if resposta.lower() == 's':
        respostas_positivas += 1

if respostas_positivas == 2:
    print("Suspeita")
elif 3 <= respostas_positivas <= 4:
    print("Cúmplice")
elif respostas_positivas == 5:
    print("Assassino")
else:
    print("Inocente")


# Exercício 02
notas_alunos = []

for _ in range(5):
    notas = [
        float(input(f"Digite a nota {i + 1} do aluno {_ + 1}: ")) for i in range(4)]
    media = sum(notas) / 4
    notas_alunos.append(media)

alunos_aprovados = sum(1 for nota in notas_alunos if nota >= 7.0)

print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")


#Exercício 03
carrinho_de_compras = {"produto1": 10,
                       "produto2": 5, "produto3": 8, "produto4": 3}

total_carrinho = sum(carrinho_de_compras.values())

print(f"Total do carrinho de compras: {total_carrinho}")


# Exercício 04
contatos = {"João": "123456789", "Maria": "987654321", "Pedro": "555555555"}

nome_pesquisa = input("Digite o nome para procurar o contato: ")

if nome_pesquisa in contatos:
    print(f"Telefone de {nome_pesquisa}: {contatos[nome_pesquisa]}")
else:
    print("Contato não encontrado.")


# Exercício 05
tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')

nova_tupla = tupla1 + tupla2

print("Nova Tupla:", nova_tupla)


# Exercício 06
nome_usuario = input("Digite seu nome: ")

nome_reverso = nome_usuario[::-1].upper()

print("Nome do usuário de trás para frente (em maiúsculas):", nome_reverso)
