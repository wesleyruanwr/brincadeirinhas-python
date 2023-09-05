from time import sleep
def maior(*num):
    c = mai = 0
    print('-=' *30)
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.5)
        c += 1
        if valor > mai:
            mai = valor
    print()
    print(f'Você digitou {c} valores', flush=True)
    sleep(1)
    print(f'E o maior deles foi {mai}', flush=True)
    sleep(1)
    print('-=' *30)


maior(4, 6, 1, 8, 4, 6, 3)
maior(1, 5, 7, 0, 3, 2, 46, 17, 90)