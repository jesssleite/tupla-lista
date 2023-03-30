LISTA_DEFAULT = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

if __name__ == '__main__':
    # intervalo de 1 a 9
    print(LISTA_DEFAULT[1:10])

    # intervalo de 8 a 13
    print(LISTA_DEFAULT[8:14])

    # números pares
    print(LISTA_DEFAULT[::2])

    # números impares
    print(LISTA_DEFAULT[1::2])

    # todos os multiplos de 2, 3 e 4
    for value in LISTA_DEFAULT:
        if value == 0:
            continue
        if value % 2 == 0 or value % 3 == 0 or value % 4 == 0:
            print(value, " ", end='')

    print()
    # Lista Reverse
    print(LISTA_DEFAULT[::-1])

    # razão
    soma1 = 0
    soma2 = 0
    for value in LISTA_DEFAULT[10:]:
        soma1 = soma1 + value

    for value in LISTA_DEFAULT[3:10]:
        soma2 += value

    print(soma1 / soma2)