import os


coluna_1 = ["   ","   ","   "]
coluna_2 = ["   ","   ","   "]
coluna_3 = ["   ","   ","   "]

linhas = [coluna_1, coluna_2, coluna_3]

num_jogador = 1

def exibir_tabuleiro_em_branco():
    print()
    for l in range(len(linhas)):
        print("          ",end="")
        for c in range(len(coluna_1)): #EU PODERIA TER PEGADO OUTRA COLUNA, POIS TODAS POSSUEM 3 POSIÇÕES
            print(f"[{linhas[l][c]}]", end="")
        print()
    print()

def realizar_movimento(linha_informada, coluna_informada, num_jogador):
    print()
    movimento_bem_sucedido = True #Não retorno diretamente True ou False, porque preciso que todos os laços sejam percorridos
    for l in range(len(linhas)):  #para preencher completamente o tabuleiro
        print("          ",end="")
        for c in range(len(coluna_1)):
            if l == linha_informada and c == coluna_informada:
                if linhas[l][c] == "   ": #VERIFICANDO SE A POSIÇÃO NÃO FOI OCUPADA
                    if num_jogador == 1: 
                        linhas[l][c] = " X "
                        print(f"[ X ]", end="")
                    else: 
                        linhas[l][c] = " O "
                        print(f"[ O ]", end="")
                else:                    # CASO A POSIÇÃO JÁ TENHA SIDO OCUPADA, NÃO SERÁ POSSÍVEL REALIZAR O MOVIMENTO
                    print(f"[{linhas[l][c]}]", end="") 
                    movimento_bem_sucedido = False
            else:
                print(f"[{linhas[l][c]}]", end="")
        print()
    print()
    return movimento_bem_sucedido

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
 
    if(linha >= 0 and linha <= 2) and (coluna >= 0 and coluna <= 2): #SE O MOVIMENTO DO USUÁRIO FOR VÁLIDO
        if(realizar_movimento(linha, coluna, num_jogador)): #APENAS SE O MOVIMENTO FOR BEM-SUCEDIDO SERÁ A VEZ DO OUTRO JOGADOR JOGAR
           num_jogador = 1 if num_jogador == 2 else 2 #TROCANDO A VEZ DO JOGADOR
        else:
            print("Movimento inválido! Essa posição já está ocupada.")
    else:
        print("Movimento inválido! Os valores válidos para lin e col vão de 1 a 3.")