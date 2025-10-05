nome = "Matheus"
nome_completo = "Matheus Ribeiro da Fonseca"

print(nome.upper()) #Maiusculo
print(nome.lower()) #Minusculo
print(nome[0]) #pegar o elemento 0 da minha variável

print(nome_completo.count("s")) #Contar os elementos
print(nome_completo.find("s")) #Encontrar o elemento dentro da string
print(nome_completo.encode()) #codificar a string em byte e para decodificar usamos o metodo encode
print(nome_completo.replace("a", "e")) #Substituindo a letra A da minha variável pela letra e
print("-".join(nome_completo)) #Colocando um separador - na minha variável
print(nome_completo.split(" ")) #dividir a string em uma lista, com base em um carecter
print(nome_completo.strip("M")) #Vai retirar elementos no inicio
print("z" in nome_completo) #Verificar se existe um elemento na variável