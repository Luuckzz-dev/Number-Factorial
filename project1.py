# Programa que calcula o fatorial de um número

number_Fat = int(input('Digite o número que você deseja saber o fatorial: '))
if number_Fat > 0:
    fatorial = 1
    for item in range(1, number_Fat +1):
        fatorial = fatorial * item
    print(fatorial)
