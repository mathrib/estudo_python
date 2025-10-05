def saudacao(nome):
    print(f"Olá, meu nome é {nome}")
    
print("Chamando a função saudacao")
saudacao("Mateus")
saudacao("Davi")
    
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("Chamando a função")
operacao = quadrado(5)
print(f"O resultado da função é {operacao}")


def soma(num1, num2):
    resultado = num1 + num2
    return resultado

print("A soma é:", soma(5,9))