# Exercício 01
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O maior número é: {num1}")
else:
    print(f"O maior número é: {num2}")

#Exercício 02
turno = input(
    "Em que turno você estuda? (M - matutino, V - vespertino, N - noturno): ").upper()

if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")

# Exercício 03
while True:
    nota = float(input("Digite uma nota de 0 a 10: "))
    if 0 <= nota <= 10:
        break
    else:
        print("Valor inválido. Digite novamente.")

print(f"Você digitou uma nota válida: {nota}")


# Exercício 04
nota = float(input("Digite a nota do aluno (de 0 a 10): "))

if nota >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado.")


# Exercício 05
lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

if lado1 == lado2 == lado3:
    print("Triângulo Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")


# Exercício 06
login = input("Digite o login: ")
senha = input("Digite a senha: ")

if login == "admin" and senha == "admin123":
    print("Acesso permitido!")
else:
    print("Erro de autenticação. Acesso negado.")


# Exercício 07
idade = int(input("Digite a sua idade: "))

if idade < 12:
    print("Criança")
elif 12 <= idade < 18:
    print("Adolescente")
elif 18 <= idade < 60:
    print("Adulto")
else:
    print("Idoso")


# Exercício 08
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior_numero = max(num1, num2, num3)

print(f"O maior número é: {maior_numero}")


# Exercício 09
num_pares = 0
num_impares = 0

while True:
    numero = int(input("Digite um número (ou zero para encerrar): "))

    if numero == 0:
        break

    if numero % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1

print(f"Números pares: {num_pares}")
print(f"Números ímpares: {num_impares}")


# Exercício 10
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

numeros_ordenados = sorted([num1, num2, num3])

print("Números em ordem crescente:", numeros_ordenados)
