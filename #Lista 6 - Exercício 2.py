inteiros = [0]*10

for i in range(9, -1, -1):
    inteiros[i] = int(input(f'Informe um número inteiro: '))

print(f'Os números, em ordem inversa ao informado são: {inteiros}')
