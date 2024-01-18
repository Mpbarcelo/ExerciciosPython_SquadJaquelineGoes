# # Exercicio 01
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print(f'Soma: {soma}')
print(f'Subtração: {subtracao}')
print(f'Multiplicação: {multiplicacao}')
print(f'Divisão: {divisao}')


# # Exercicio 02
ano_nascimento = int(input('Digite o ano de nascimento: '))
idade_atual = 2024 - ano_nascimento
print(f'Sua idade atual é: {idade_atual} anos')


# # exercicio 03
quilometros = float(input('Digite a quantidade de quilômetros: '))
metros = quilometros * 1000
centimetros = quilometros * 100000
milimetros = quilometros * 1000000

print(f'{quilometros} quilômetros são equivalentes a:')
print(f'{metros} metros')
print(f'{centimetros} centímetros')
print(f'{milimetros} milímetros')


# #exercicio 04
litros = float(
    input('Digite a quantidade de litros de combustível consumidos: '))
distancia = float(input('Digite a distância percorrida em quilômetros: '))

consumo_medio = distancia / litros

print(f'O consumo médio é de {consumo_medio:.2f} km/l')

# #exercicio 05
salario_bruto = float(input('Digite o salário bruto: '))
desconto_ir = 0.0

if salario_bruto <= 1903.98:
    desconto_ir = 0
elif 1903.99 <= salario_bruto <= 2826.65:
    desconto_ir = 7.5
elif 2826.66 <= salario_bruto <= 3751.05:
    desconto_ir = 15
elif 3751.06 <= salario_bruto <= 4664.68:
    desconto_ir = 22.5
else:
    desconto_ir = 27.5

salario_liquido = salario_bruto * (1 - desconto_ir / 100)

print(f'O salário líquido é de R${salario_liquido:.2f}')


# #exercicio 06
distancia_viagem = float(
    input('Digite a distância da viagem em quilômetros: '))

tempo_aviao = distancia_viagem / 600
tempo_carro = distancia_viagem / 100
tempo_onibus = distancia_viagem / 80

print(f'Tempo de viagem de avião: {tempo_aviao:.2f} horas')
print(f'Tempo de viagem de carro: {tempo_carro:.2f} horas')
print(f'Tempo de viagem de ônibus: {tempo_onibus:.2f} horas')


# #exercicio 07
peso = float(input('Digite o peso em kg: '))
altura = float(input('Digite a altura em metros: '))

imc = peso / (altura * altura)

print(f'O Índice de Massa Corporal (IMC) é: {imc:.2f}')

# #exercicio 08
valor_por_hora = float(input('Digite quanto você ganha por hora: '))
horas_trabalhadas = float(
    input('Digite o número de horas trabalhadas no mês: '))

salario_mensal = valor_por_hora * horas_trabalhadas

print(f'O salário mensal é de R${salario_mensal:.2f}')


# #exercicio 09
horas_semana = float(
    input('Digite o número de horas de exercício físico por semana: '))

calorias_por_minuto = 5
calorias_mensais = horas_semana * 4 * 7 * calorias_por_minuto

print(f'Total de calorias queimadas em um mês: {calorias_mensais} calorias')


# #exercicio 10
nome = "Maria"
idade = 25
lugar = "São Paulo"
profissao = "engenheira"

print(f'Olá {nome}, prazer te conhecer. Tenho {idade} anos e sou de {lugar}. Atualmente, trabalho como {profissao}.')
