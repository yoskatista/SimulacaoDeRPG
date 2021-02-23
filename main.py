nome = 'maico'
vida = 20
ataque = 3
defesa = 2
vivo  = True


def atacar():
    print('Eu vou matar goblins')


def coletar():
    print('Vou coletar materiais')


def resgatar():
    print('Vou resgatar inocentes')


def main():
    print('\nOlá como posso ajudar?')
    print('\nmissões:')
    print('1 matar goblins')
    print('2 coletar materiais')
    print('3 resgatar inocentes')

    resposta = int(input('Eu escolho: '))
    if resposta == 1:
        atacar()
    elif resposta == 2:
        coletar()
    elif resposta == 3:
        resgatar()
    else:
        print('Não tem essa opção')



loop = True
while loop:
    main()