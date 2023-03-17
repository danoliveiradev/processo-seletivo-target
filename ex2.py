import json

# Converte json em dicionario
with open("dados.json") as dados: dadosFaturamento = json.load(dados)
dadosValor = []
maiorValor = 0
menorValor = 0
soma = 0
media = 0
numDias = 0

# Filtra os valores positivos
for i in dadosFaturamento:
    if i['valor'] > 0:
        dadosValor.append(i['valor'])

# Calcula maior  e menor valores
menorValor = min(dadosValor)
maiorValor = max(dadosValor)

# Soma valores
for c in dadosValor:
    soma += c

# Calcula média
media = soma / len(dadosValor)

# Determina número de dias acima da média
for c in dadosValor:
    if c > media:
        numDias += 1

print(f'O menor valor diário faturado foi: {menorValor}')
print(f'O maior valor diário faturado foi: {maiorValor}')
print(f'Número de dias acima da média mensal: {numDias}')

print(media)