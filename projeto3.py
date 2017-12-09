try:
    arquivo = open('car.txt','r')
    carros = arquivo.readlines()

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
        if carros[i][0] > preco:
            elimina = True
        elif carros[i][1] > manutencao:
            elimina = True
        elif carros[i][2] < portas:
            elimina = True
        elif carros[i][3] < pessoas:
            elimina = True
        elif carros[i][4] < mala:
            elimina = True
        elif carros[i][5] < seguranca:
            elimina = True

        if elimina == True:
            indesejados.append(i)

    indesejados.reverse()
    for j in indesejados:
        carros.pop(j)
    arquivo.close()
    print(carros)
except IOError:
    print ("ERRO em arquivo -")
