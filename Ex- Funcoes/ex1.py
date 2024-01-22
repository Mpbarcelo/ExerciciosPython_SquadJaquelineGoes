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