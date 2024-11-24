import os

#TODO: Implementar método de reinicar o jogo
#TODO: Refatorar método realizar_movimento() de modo que ele não realize tantas funções como: verificar se a posição já está ocupada
#                                                                                                      imprimir o tabuleiro na tela...

coluna_1 = ["   ","   ","   "]
coluna_2 = ["   ","   ","   "]
coluna_3 = ["   ","   ","   "]
linhas = [coluna_1, coluna_2, coluna_3]

combinacoes_vencedoras = [[ [0,0],[0,1],[0,2] ], [ [1,0],[1,1],[1,2] ], [ [2,0],[2,1],[2,2] ],#comb.horizontais
                          [ [0,0],[1,0],[2,0] ], [ [0,1],[1,1],[2,1] ], [ [0,2],[1,2],[2,2] ],#comb.verticais
                          [ [0,2],[1,1],[2,0] ], [ [0,0],[1,1],[2,2] ]] #comb. diagonais
posicoes_x = [] #Preciso saber todas as posições do X para verificar se as posições se encaixam nas combinações vencedoras
posicoes_o = [] #Preciso saber todas as posições do Y para verificar se as posições se encaixam nas combinações vencedoras
num_jogador = 1
jogadas_realizadas = 0 #Conta a quantidade de jogadas realizadas para saber se houve empate. Obs.: 9 == empate
empate = False         #Variável para reconhecer se houve empate ou não

def exibir_tabuleiro_em_branco():
    print()
    for l in range(len(linhas)):
        print("          ",end="")
        for c in range(len(coluna_1)): #Poderia ter selecionado qualquer outra coluna, pois todas possuem 3 posições. 
            print(f"[{linhas[l][c]}]", end="")
        print()
    print()

def realizar_movimento(linha_informada, coluna_informada, num_jogador):
    print()
    movimento_bem_sucedido = True #Não retorno diretamente True ou False, porque preciso que todos os laços sejam percorridos
    for l in range(len(linhas)):  #para preencher completamente o tabuleiro
        print("          ",end="")
        for c in range(len(coluna_1)):
            if l == linha_informada and c == coluna_informada: #Posição selecionada pelo jogador foi encontrada
                if linhas[l][c] == "   ": #Verificando se a posição não está ocupada
                    if num_jogador == 1: 
                        linhas[l][c] = " X "
                        posicoes_x.append([l, c]) #Salvando as posições em que o 'X' está posicionado
                        print(f"[ X ]", end="")
                    else: 
                        linhas[l][c] = " O "
                        posicoes_o.append([l, c]) #Salvando as posições em que o 'O' está posicionado
                        print(f"[ O ]", end="")
                else:                    # Caso a posição já tenha sido ocupada, não será possível realizar o movimento
                    print(f"[{linhas[l][c]}]", end="") 
                    movimento_bem_sucedido = False
            else:
                print(f"[{linhas[l][c]}]", end="")
        print()
    print()
    return movimento_bem_sucedido


def verificar_vencedor():
    counter = 0; #Conta a quantidade de vezes que a posicao do X/O está presente na combinação vencedora atual. Obs.: 3 == vitória
    for combinacao_vencedora in combinacoes_vencedoras: 
        for posicao_x in posicoes_x: 
            if posicao_x in combinacao_vencedora:
                counter += 1
        if counter == 3: #Caso o jogador X tenha sido o vencedor
            print(f"{"-" * 10} O JOGADOR 'X' FOI O VENCEDOR {"-" * 10}")
            print()
            return True
        else:
            counter = 0 #Zerando o contador para poder verificar se o Jogador 'O' foi o vencedor
        for posicao_o in posicoes_o: 
            if posicao_o in combinacao_vencedora:
                counter += 1
        if counter == 3: #Caso o jogador X tenha sido o vencedor
            print(f"{"-" * 10} O JOGADOR 'O' FOI O VENCEDOR {"-" * 10}\n\n")

            return True
        else:
            counter = 0 #Zerando o contador para poder verificar se o Jogador 'X' foi o vencedor
    return False


os.system('cls')
print("BEM-VINDO AO JOGO DA VELHA")
print("OS NÚMEROS POSSÍVEIS PARA LINHA E COLUNA VÃO DE 1 À 3")
exibir_tabuleiro_em_branco()


while(True):

    print(f"\nVEZ DO JOGADOR {"'X'" if num_jogador == 1 else "'O'"}")
    
    posicao = input("Digite a posição para onde deseja se mover (lin,col): ")
    if not " " in posicao:
        movimento = posicao.split(",")
    else:
        print("Não coloque nenhum espaço entre a posição da linha e coluna. Use apenas uma vírgula!")
        continue

    
    try:
        linha = int(movimento[0]) - 1    
        coluna = int(movimento[1]) - 1    
        #Coloquei lin/col - 1 para que o usuário não tenha que ficar pensando que a 1ª linha é a linha 0, 1ª coluna é coluna 0...
    except:
        print("Digite os dados neste formato: (1,1) (2,2) (1,2)")
        continue
 
    if(linha >= 0 and linha <= 2) and (coluna >= 0 and coluna <= 2): #Se o movimento do usuário for válido
        if(realizar_movimento(linha, coluna, num_jogador)): #Verificando se o movimento foi bem-sucedido
           
            jogadas_realizadas += 1 # Contando a quantidade de jogadas para verificar situação de empate
            empate = True if jogadas_realizadas == 9 else False
            
            if verificar_vencedor(): #Verificando se houve um vencedor ou empate entre os jogadores
                break

            if empate:
                print(f"{"-" * 10} NÃO HOUVE VENCEDOR NESTA RODADA! {"-" * 10}\n\n")
                break
            else:
                num_jogador = 1 if num_jogador == 2 else 2 #Trocando a vez do jogador caso não haja vencedor nem empate         
            
        else:
            print("Movimento inválido! Essa posição já está ocupada.")
    else:
        print("Movimento inválido! Os valores válidos para lin e col vão de 1 a 3.")