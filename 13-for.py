lista = [1,2,3,4,5]
for elemento in lista:
    print(elemento)
    
for numero in range(0,10):
    print(numero)

for indice in range(0, len(lista)):
    print("Indice:", indice)
    print("Elemento:", lista[indice])
    

#enumerate
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print("Indice:", indice)
    print("Valor:", valor)