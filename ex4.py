dadosfaturamento = [{'estado':'SP', 'valor':67836.43},
                    {'estado':'RJ','valor':36678.66},
                    {'estado':'MG','valor':29229.88},
                    {'estado':'ES','valor':27165.48},
                    {'estado':'outros','valor':19849.53}]

valorTotal = 0
percentual = 0

# Soma os valores dos Estados
for i in dadosfaturamento:
    valorTotal += i['valor']

# Realiza o calculo de participação percentual
for c in dadosfaturamento:
    percentual = (c['valor'] / valorTotal) * 100
    print(f"Estado: {c['estado']}")
    print(f"Valor: R$ {c['valor']}")
    print(f'Representação: {percentual:.2f}%')
    print('-=-'*20)
