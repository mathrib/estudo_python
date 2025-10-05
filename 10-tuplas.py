tupla = (1,2,2,3,4)
print(tupla)
print(f"minha tupla é {tupla}")
print(f"O primeiro valor da minha tupla é {tupla[0]}")
print(f"O último valor da minha tupla é {tupla[-1]}")

#Método count - conta quantos elementos aparece na tupla
contagem = tupla.count(2)
print(contagem)

#Método index - pega o índice do elemento
indice = tupla.index(2)
print(indice)