num = int(input('Digite um número inteiro: '))
numSeq = 0
fb = [0]
status = False

if len(fb) == 1:
    fb.append(1)
    numSeq = 1

# Calcula os valores da sequencia de Fibonacci até o primeiro valor maior que o número digitado
while numSeq <= num:
    numSeq = fb[len(fb) - 2] + numSeq
    fb.append(numSeq)

# Verifica se o número é Fibonacci
for i in fb:
    if i == num:
        print(f'O número {num} pertence a sequência  de Fibonacci.')
        status = True
        break

if status == False:
    print(f'O número {num} NÃO pertence a sequência de Fibonacci.')
