def ex_1():
    n1 = float(input('Digite um número:'))
    n2 = float(input('Digite outro número:'))

    if n1 > n2:
        print('O maior número é:', n1)
    else:
        print('O maior número é:', n2)


def ex_2():
    valor = float(input('Digite um valor qualquer:'))

    if valor < 0:
        print('O valor é negativo')
    elif valor > 0:
        print('O valor é positivo')
    else:
        print('O valor é nulo')


def ex_3():
    sexo = input('Digite seu sexo:').upper()

    if sexo =='F':
        print('Sexo Feminino')
    elif sexo == "M":
        print('Sexo Masculino')
    else:
        print('Degite um sexo válido')


def ex_4():
    letra = input('Digite uma letra').lower()

    if len(letra) >= 2:
        print('DIGITE APENAS UMA LETRA')

    if letra == 'a' or 'e' or 'i' or 'o' or 'u':
        print('A letra é uma vogal')
    else:
        print('A letra é uma consoante')


def ex_5():
    n1 = float(input('Digite a primeira nota:'))
    n2 = float(input('Digite a segunda nota:'))

    media = (n1 + n2) / 2

    if media == 10:
        print('Aluno aprovado com destinção.')
    elif media >= 7:
        print('O aluno está aprovado.')
    else:
        print('Aluno reprovado.')


def ex_6():
    n1 = float(input('Digite o primeiro número:'))
    n2 = float(input('Digite o segundo número:'))
    n3 = float(input('Digite o terceiro número:'))

    if n1 > n2 and n1 > n3:
        print('O maior número é: ', n1)
    elif n2 > n1 and n2 > n3:
        print('O maior número é: ', n2)
    else:
        print('O maior número é: ', n3)


def ex_7():
    n1 = float(input('Digite o primeiro número:'))
    n2 = float(input('Digite o segundo número:'))
    n3 = float(input('Digite o terceiro número:'))

    if n1 > n2 and n1 > n3:
        if n2 < n3:
            print('O maior número é {} e o menor é {}.'.format(n1,n2))
        else:
            print('O maior número é {} e o menor é {}.'.format(n1,n3))

    elif n2 > n1 and n2 > n3:
        if n1 < n3:
            print('O maior número é {} e o menor é {}.'.format(n2,n1))
        else:
            print('O maior número é {} e o menor é {}.'.format(n2,n3))
    elif n3 > n1 and n3 > n2:
        if n2 < n1:
            print('O maior número é {} e o menor é {}.'.format(n3,n2))

        else:
            print('O maior número é {} e o menor é {}.'.format(n3,n1))


def ex_8():
    preco1 = float(input('Digite o preco do primeiro produto: '))
    preco2 = float(input('Digite o preco do segundo produto: '))
    preco3 = float(input('Digite o preco do terceiro produto: '))

    if preco1 < preco2 and preco1 < preco3:
        print('Comprar o primeiro produto')
    elif preco2 < preco1 and preco2 < preco3:
        print('Comprar o segundo produto')
    else:
        print('Comprar o terceiro produto')


def ex_9():
    n1 = float(input('Digite o primeiro número:'))
    n2 = float(input('Digite o segundo número:'))
    n3 = float(input('Digite o terceiro número:'))

    if n1 < n2 and n1 < n3:
        print('O maior número é: ', n1)
    elif n2 < n1 and n2 < n3:
        print('O maior número é: ', n2)
    else:
        print('O maior número é: ', n3)


def ex_10():
    print('M - Matutino')
    print('V - Vespertino')
    print('N - Noturno')
    turno = input('Digite o Turno que você estuda: ').upper()

    if turno == 'M':
        print('Bom Dia!')
    elif turno == 'V':
        print('Boa Tarde!')
    elif turno == 'N':
        print('Boa Noite!')
    else:
        print('Digite um turno válido.')


def ex_11():

    def printa_salario(salario, aumento):
        salario_reajustado = salario * aumento
        print(f'''O sálario sem reajuste é: R${salario}
                O valor do aumento é: R${salario*(aumento - 1)}
                O sálario reajustado é de: R${salario_reajustado}''')

    salario = float(input('Digite o sálario: '))

    if salario < 280:
        aumento = 1.2
        printa_salario(salario, aumento)

    elif salario >=280 and salario < 700:
        aumento = 1.15
        printa_salario(salario,aumento)
    
    elif salario >= 700 and salario < 1500:
        aumento = 1.1
        printa_salario(salario,aumento)

    else:
        aumento = 1.05
        printa_salario(salario,aumento)

def ex_12():
    pass


def ex_13():
    numero = int(input('Digite um número correspondente a um dia da semana: '))

    if numero == 1:
        print('1 - Domingo')
    elif numero == 2:
        print('2 - Segunda')
    elif numero == 3:
        print('3 - Terça')
    elif numero == 4:
        print('4 - Quarta')
    elif numero == 5:
        print('5 - Quinta')
    elif numero == 6:
        print('6 - Sexta')
    elif numero == 7:
        print('7 - Sábado')
    else:
        print('Digite um número válido')


def ex_14():
    def printa_nota(nota, conceito):
        print('Média: ', media)
        print('Conceito: ', conceito)
        if conceito == "A" or 'B' or 'C':
            print('Situação: Aprovado')
        else:
            print('Situação: Reprovado')

    nota_1 = float(input('Digite a primeira nota: '))
    nota_2 = float(input('Digite a segunda nota: '))

    media = (nota_1 + nota_2) / 2

    if media == 10 and media >= 9 :
        conceito = 'A'
        printa_nota(media, conceito)
    elif media < 9 and media >= 7.5:
        conceito = 'B'
        printa_nota(media, conceito)
    elif media < 7.5 and media >= 6:
        conceito = 'C'
        printa_nota(media,conceito)
    elif media < 6 and media >= 4:
        conceito = 'D'
        printa_nota(media, conceito)
    else:
        conceito ='E'
        printa_nota(media,conceito)

