pessoa = {"nome":"Matheus", "idade": 25, "cidade":"Natal"}
print(f"Meu dicionário de exemplo é {pessoa}")
print(f"O meu nome é {pessoa['nome']}")
print(f"Minha idade é {pessoa['idade']}")

pessoa["sobrenome"] = "Ribeiro"
print(pessoa)

#Atualizar dados
pessoa["idade"] = 26
print(pessoa)

#removendo um par chave-valor
del pessoa["sobrenome"]
print(pessoa)

#Métodos keys(), values() e items()
chaves = list(pessoa.keys())
print(f"Chaves do meu dicionário {chaves}")
print(f"A primeira chave é {chaves[0]}")

valores = list(pessoa.values())
print(f"Os valores do meu dicionário é {valores}")

#Métodos items
itens = list(pessoa.items())
print(itens)