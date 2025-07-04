
# Função para calcular as aliquotas
def calcular_imposto(salario):
    aliquota = 0.00
    if (salario >= 0 and salario <= 1100):
        aliquota = 0.05
    elif (salario >= 1100 and salario <= 2500):
       aliquota = 0.10
    else:
        aliquota = 0.15
    return aliquota * salario

# Ler os valores de entrada
valor_salario = float(input())
valor_beneficio = float(input())

valor_imposto = calcular_imposto(valor_salario)
# Calcula e imprime a saída (com duas casas decimais)
saida = valor_salario - valor_imposto + valor_beneficio
print(f"{saida:.2f}")