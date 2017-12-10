def converte(atributo,dado):
    if atributo == 1 or atributo == 2:
        if dado == 1:
            dado = "baixo"
        elif dado == 2:
            dado = "medio"
        elif dado == 3:
            dado = "alto"
        else:
            dado = "muito alto"
    elif atributo == 3 or atributo == 4:
        dado = str(dado)
    elif atributo == 5:
        if dado == 1:
           dado = "pequena"
        elif dado == 2:
            dado = "media"
        else:
            dado = "grande"
    else:
        if dado == 1:
           dado = "pequena"
        elif dado == 2:
            dado = "media"
        else:
            dado = "alta"
    return dado

try:
    arquivo = open('car.txt','r')
    carros = arquivo.readlines()

    prioridade = input("Defina uma ordem de prioridade para os atributos:\n1 - Preço\n2 - Custo da manutenção\n3 - Numero Portas\n4 - Numero de Pessoas\n5 - Capacidade Mala\n6 - Nível de Segurança\n")
    prioridade = prioridade.split(',')
    prioridade = [int(i) for i in prioridade]

    preco = int(input("Qual a media de preço do carro que você procura? Escolha entre as opções abaixo:\n1-baixo\n2-medio\n3-alto\n4-muito alto\n"))
    while preco < 1 or preco > 4:
        preco = int(input("Qual a media de preço do carro que você procura? Escolha entre as opções abaixo:\n1-baixo\n2-medio\n3-alto\n4-muito alto\n")) 

    manutencao = int(input("Qual a media de preço de manuntenção que você procura? Escolha entre as opções abaixo:\n1-baixo\n2-medio\n3-alto\n4-muito alto\n"))
    while manutencao < 1 or manutencao > 4:
        manutencao = int(input("Qual a media de preço de manuntenção que você procura? Escolha entre as opções abaixo:\n1-baixo\n2-medio\n3-alto\n4-muito alto\n"))

    portas = int(input("Qual a quantidade de portas do carro que você procura? Escolha entre as opções abaixo:\n2-duas portas\n3-três portas\n4-quatro portas\n5-cinco portas ou mais\n"))
    while portas < 2 or portas > 5:
        portas = int(input("Qual a quantidade de portas do carro que você procura? Escolha entre as opções abaixo:\n2-duas portas\n3-três portas\n4-quatro portas\n5-cinco portas ou mais\n"))

    pessoas = int(input("Qual a capacidade de pessoas no carro que você procura? Escolha entre as opções abaixo:\n2-duas pessoas\n4-quatro pessoas\n5-cinco pessoas ou mais\n"))
    while pessoas < 2 or pessoas > 5:
        pessoas = int(input("Qual a capacidade de pessoas no carro que você procura? Escolha entre as opções abaixo:\n2-duas pessoas\n4-quatro pessoas\n5-cinco pessoas ou mais\n"))

    mala = int(input("Qual a capacidade da mala do carro que você procura? Escolha entre as opções abaixo:\n1-pequena\n2-media\n3-grande\n"))
    while mala < 1 or mala > 3:
        mala = int(input("Qual a capacidade da mala do carro que você procura? Escolha entre as opções abaixo:\n1-pequena\n2-media\n3-grande\n"))

    seguranca = int(input("Qual o nível de segurança do carro que você procura? Escolha entre as opções abaixo:\n1-pequena\n2-media\n3-alta\n"))
    while seguranca < 1 or seguranca > 3:
        seguranca = int(input("Qual o nível de segurança do carro que você procura? Escolha entre as opções abaixo:\n1-pequena\n2-media\n3-alta\n"))

    indesejados = []
    for i in range(len(carros)):
        carros[i] = carros[i].split(",")
        carros[i].pop()
        ################ Transformacoes dos dados ##########################
        if carros[i][0] == "vhigh":
            carros[i][0] = 4
        elif carros[i][0] == "high":
            carros[i][0] = 3
        elif carros[i][0] == "med":
            carros[i][0] = 2
        else:
            carros[i][0] = 1

        if carros[i][1] == "vhigh":
            carros[i][1] = 4
        elif carros[i][1] == "high":
            carros[i][1] = 3
        elif carros[i][1] == "med":
            carros[i][1] = 2
        else:
            carros[i][1] = 1

        carros[i][2] = int(carros[i][2])
        carros[i][3] = int(carros[i][3])

        if carros[i][4] == "big":
            carros[i][4] = 3
        elif carros[i][4] == "med":
            carros[i][4] = 2
        else:
            carros[i][4] = 1

        if carros[i][5] == "high":
            carros[i][5] = 3
        elif carros[i][5] == "med":
            carros[i][5] = 2
        else:
            carros[i][5] = 1

        ################ Eliminacao dos carros que nao interessam ##########################
        elimina = False
        if carros[i][0] < preco-1 or carros[i][0] > preco+1:
            elimina = True
        elif carros[i][1] < manutencao-1 or carros[i][1] > manutencao+1:
            elimina = True
        elif carros[i][2] < portas-1 or carros[i][2] > portas+1:
            elimina = True
        elif carros[i][3] < pessoas-1 or carros[i][3] > pessoas+1:
            elimina = True
        elif carros[i][4] < mala-1 or carros[i][4] > mala+1:
            elimina = True
        elif carros[i][5] < seguranca-1 or carros[i][5] > seguranca+1:
            elimina = True

        if elimina == True:
            indesejados.append(i)

    indesejados.reverse()
    for j in indesejados:
        carros.pop(j)
    arquivo.close()

    while len(carros) > 5:
        opcao1 = carros[0]
        opcao2 = carros[len(carros)-1]
        print("Escolha um desses carros:")
        print("1-Preço: %s; Manutenção: %s; Portas: %s; Pessoas: %s; Mala: %s; Segurança: %s"
              %(converte(1,opcao1[0]),converte(2,opcao1[1]),converte(3,opcao1[2]),converte(4,opcao1[3]),converte(5,opcao1[4]),converte(6,opcao1[5])))
        print("2-Preço: %s; Manutenção: %s; Portas: %s; Pessoas: %s; Mala: %s; Segurança: %s"
              %(converte(1,opcao2[0]),converte(2,opcao2[1]),converte(3,opcao2[2]),converte(4,opcao2[3]),converte(5,opcao2[4]),converte(6,opcao2[5])))
        escolha = int(input())
        if escolha == 1:
            carros = carros[0:len(carros)//2]
        else:
            carros = carros[len(carros)//2:]              
            
    print(carros)
    print(prioridade)
    
except IOError:
    print ("ERRO em arquivo -")
