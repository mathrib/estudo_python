lista = [1,3,4,5,"blip",True,False]

#Método append - Adiciona um elemento no final da lista
lista.append(6)
print(lista)

#Método Index - Pega o índice de um elemento
indice = lista.index("blip")
print(indice)

#Método Insert - Insere o elemento em um índice específico
lista.insert(4, "Blip GO")
print(lista)

#Método pop - Remove e retorna um elemento de um índice específico
elemento = lista.pop(3)
print(elemento)
print(lista)

#Método remove - Remove o elemento
lista.remove(True)
print(lista)

#Metodo short - Ordena a lista em ordem crescente
