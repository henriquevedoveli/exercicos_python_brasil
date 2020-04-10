def ex_1():
    return print('Alô Mundo')


def ex_2():
    numero = float(input('Digite um número:'))
    return print(f'O número informado foi: {int(numero)}')


def ex_3():
    n1 = float(input("Digite o primeiro número:"))
    n2 = float(input("Digite o segundo número:"))

    soma = n1 + n2

    return print(f"A soma de {n1} e {n2} é {soma}")


def ex_4():
    n1 = float(input("Digite a primeira nota:"))
    n2 = float(input("Digite a segunda nota:"))
    n3 = float(input("Digite a terciera nota:"))
    n4 = float(input("Digite a quarta nota:"))

    soma = n1 + n2 + n3 + n4
    media = soma / 4

    print("A média das quatros notas é:", media)


def ex_5():
    metros = float(input("Metros:"))

    # metros -> centimetros (1m = 100cm)
    centimetros = metros * 100

    return print(f'{metros} metros são {centimetros} centimetros.')


def ex_6():
    raio = float(input("Raio:"))

    # area = pi*r^2 (pi \approx 3,1416)
    area = 3.1416 * (raio * raio)

    return print(f"Um circúlo com raio {raio}, tem área {area}.")


def ex_7():
    lado = float(input("Digite o tamaho do lado:"))

    area = lado * lado

    return print(f"O dobro da área é {2 * area}")


def ex_8():
    horas = int(input("Número de horas trabalhadas esse mês:"))
    salario_hora = float(input("Quanto você ganha por hora:"))

    return print(f"Seu sálario desse mês é R${horas * salario_hora}")


def ex_9():
    faren = float(input("Digite a temperatura em graus Farenheit: "))
    cel = (5 * (faren - 32) / 9)
    return print(f'{faren} graus Farenheit são {cel} graus Celsius')


def ex_10():
    cel = float(input("Digite a temperatura em graus Celsius: "))
    faren = (cel * (9/5)) + 32
    return print(f'{cel} graus Celsius são {faren} graus Farenheit')


def ex_11():
    n1_int = int(input('Digite um número inteiro:'))
    n2_int = int(input('Digite outro número inteiro:'))
    n3_float = float(input('Digite um número real:'))

    #a)
    # produto do dobro do primeiro com a metade do segundo
    prod= (n1_int *2) * (n2_int/2)

    #b)
    # soma do triplo do primeiro com o terceiro
    soma = (3*n1_int) + n3_float

    #c)
    #o terceiro elevado ao cubo
    cubo = n3_float**3

    return print(f'O produto do dobro do primeiro com a metade do segundo é {prod} /n'
                 f'A soma do triplo do primeiro com o terceiro é {soma}/n'
                 f'O terceiro elevado ao cubo é {cubo}')


def ex_12():
    altura = float(input('Digite sua altura em metros:'))

    peso_ideal = (72.7*altura) - 58

    return print('Seu peso ideal é:', peso_ideal)









