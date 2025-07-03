# FUNÇAO QUE DEFINE A ESCOLHA DE SERVIÇO
def escolha_servico():
    # ENTRADA DAS OPÇÕES
    servico = input('>> ').lower()
    
    # LAÇO DE REPETIÇÃO E ESTRUTURA CONDICIONAL PARA QUANDO O USUÁRIO DEFINIR QUAL SERVIÇO ESCOLHIDO
    while servico not in ('dig', 'ico', 'ipb', 'fot'):
        print('Escolha inválida, entre com o tipo de serviço novamente')
        return escolha_servico()
    if servico == ('dig'):
        valor = 1.10
    elif servico == ('ico'):
        valor = 1.00
    elif servico == ('ipb'):
        valor = 0.40
    elif servico == ('fot'):
        valor = 0.20
    return(valor)

# FUNÇÃO EM QUE O USUÁRIO DEFINE O DESCONTO DE ACORDO COM A QUANTIDADE DE PÁGINAS
def num_pagina():
    while True:
        try:
            # ENTRADA PARA O USUÁRIO DIGITAR A QUANTIDADE DE PÁGINAS E CONDICIONAIS
            paginas = int(input('Entre com o número de páginas: \n'))

            if (paginas < 20):
                desconto = 0
            elif (paginas >= 20) and (paginas < 200):
                desconto = 0.15
            elif (paginas >= 200) and (paginas < 2000):
                desconto = 0.20
            elif (paginas >= 2000) and (paginas < 20000):
                desconto = 0.25
            elif (paginas >= 20000):
                print('Quantidade de páginas não permitida.\n Por favor, tente novamente.')
                continue
        # CASO O USUÁRIO DIGITE OUTRO VALOR SEM SER NÚMEROS INTEIRO
        except ValueError:
            print('Por favor insira números')
        else:
            return(paginas, desconto)


# FUNÇÃO EM QUE O USUÁRIO OPTA PELO SERVIÇO EXTRA OU NÃO
def servico_extra():
    while True:
        print('Deseja adicionar algum serviço?')
        print('1 - Encadernação Simples - R$15.00')
        print('2 - Encadernação Capa Dura R$40.00')
        print('0 - Não desejo mais nada')
        try:
            op_extra = int(input('>> '))
            if op_extra in (0, 1, 2):
                break
            else:
                print('Opção inválida. Tente novamente.')
        except ValueError:
            print('Por favor, digite um número')
    if (op_extra == 1):
        extra = 15.00
    elif (op_extra == 2):
        extra = 40.00
    else:
        extra = 0       
    return(extra)


# PROGRAMA PRINCIPAL
while True:
    print('Bem Vindo(a) a Copiadora do Adailson Ferreira\n')
    print('Entre com o tipo de serviço desejado')
    print('DIG - Digitalização')
    print('ICO - Impressora Colorida')
    print('IPB - Impressão Preto e Branco')
    print('FOT - Fotocópia\n')
    
    # VARIÁVEIS
    valor = escolha_servico()
    paginas, desconto = num_pagina()
    extra = servico_extra()

    # CÁLCULO ARITMÉTICO DO TOTAL DO VALOR
    subtotal = (valor * paginas) * desconto
    total = (valor * paginas) - subtotal + extra
    
    # SAÍDA FINAL DO PROGRAMA    
    print(f'Total = R${total:.2f} (serviço: {valor:.2f} * páginas: {paginas} + extra: {extra:.2f})')
    break