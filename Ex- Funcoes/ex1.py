# exercicio 02
def inverter_numero(numero):
    return int(str(numero)[::-1])

numero = int(input("Digite um número inteiro: "))
resultado = inverter_numero(numero)
print(f"Número invertido: {resultado}")