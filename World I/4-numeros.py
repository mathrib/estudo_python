#Inteiro
numero_inteiro = 25

#Numero real com ponto flutuante
numero_real = 6.9

print(f"Inteiro: {numero_inteiro}")
print(f"Numero Real: {numero_real}")

#Função Type
print(f"O tipo da variável {numero_inteiro} é", type(numero_inteiro))
print(f"O tipo da variável {numero_real} é", type(numero_real))

#Operações Aritimetricas
num1 = 5
num2 = 3
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print(f"A soma entre {num1} e {num2} é {soma}")
print(f"A subtração entre {num1} e {num2} é {subtracao}")
print(f"A multiplicação entre {num1} e {num2} é {multiplicacao}")
print(f"A divisão entre {num1} e {num2} é {divisao:.2f}")

print(type(divisao))
print(int(divisao)) #convertendo float em inteiro
print(float(soma)) #Convertendo inteiro em float

modulo = num1 % num2 #Resto da divisão
print(modulo)