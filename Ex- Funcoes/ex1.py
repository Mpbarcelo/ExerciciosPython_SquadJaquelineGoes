# exercicio 01
def somar_numeros(a, b, c):
    return a + b + c

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

resultado = somar_numeros(num1, num2, num3)
print(f"A soma dos três números é: {resultado}")


# exercicio 02
def inverter_numero(numero):
    return int(str(numero)[::-1])

numero = int(input("Digite um número inteiro: "))
resultado = inverter_numero(numero)
print(f"Número invertido: {resultado}")


# exercicio 03
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def menu_conversao():
    escolha = input("Escolha a opção (1 - Celsius para Fahrenheit, 2 - Fahrenheit para Celsius): ")
    
    if escolha == '1':
        temp_celsius = float(input("Digite a temperatura em Celsius: "))
        resultado = celsius_para_fahrenheit(temp_celsius)
        print(f"A temperatura em Fahrenheit é: {resultado}°F")
    elif escolha == '2':
        temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        resultado = fahrenheit_para_celsius(temp_fahrenheit)
        print(f"A temperatura em Celsius é: {resultado}°C")
    else:
        print("Opção inválida.")


menu_conversao()

# exercicio 04
def calcular_valor_em_moeda(valor_em_real, taxa_de_conversao):
    return valor_em_real / taxa_de_conversao

# Tabela de conversão
conversao_moedas = {
    "Dólar Americano": 4.91,
    "Peso Argentino": 0.02,
    "Dólar Australiano": 3.18,
    "Dólar Canadense": 3.64,
    "Franco Suíço": 0.42,
    "Euro": 5.36,
    "Libra Esterlina": 6.21
}


carteira_em_real = float(input("Digite quanto dinheiro você tem na carteira (em reais): "))

for moeda, taxa in conversao_moedas.items():
    valor_convertido = calcular_valor_em_moeda(carteira_em_real, taxa)
    print(f"Com R${carteira_em_real:.2f}, você poderia comprar {valor_convertido:.2f} {moeda}")


#exercicio 05
def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in frase if letra in vogais)


frase_usuario = input("Digite uma frase: ")
total_vogais = contar_vogais(frase_usuario)
print(f"Total de vogais na frase: {total_vogais}")

#exercicio 06
import random

def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvimento", "jogodeforca", "exercicio"]
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_corretas):
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def jogar_forca():
    palavra_secreta = escolher_palavra()
    tentativas_maximas = 6
    letras_corretas = []

    print("Bem-vindo ao Jogo da Forca!")
    print("A palavra secreta tem", len(palavra_secreta), "letras.")

    while tentativas_maximas > 0:
        palpite = input("Digite uma letra: ")

        if palpite in palavra_secreta:
            letras_corretas.append(palpite)
            print("Letra correta!")
        else:
            tentativas_maximas -= 1
            print(f"Letra incorreta! Tentativas restantes: {tentativas_maximas}")

        print("Palavra atual:", mostrar_palavra(palavra_secreta, letras_corretas))

        if all(letra in letras_corretas for letra in palavra_secreta):
            print("Parabéns! Você acertou a palavra!")
            break

    if tentativas_maximas == 0:
        print(f"Fim de jogo! Você excedeu o número máximo de tentativas. A palavra era: {palavra_secreta}")


jogar_forca()
