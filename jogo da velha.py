
tableA = ['_','_','_']
tableB = ['_','_','_']
tableC = ['_','_','_']
resp = "s"
table = [tableA,tableB,tableC]
end = False



def game():
       
        print(tableA)
        print(tableB)
        print(tableC)
    

def entrada():
    jogadas = 0
    check_vencedor = ''
            
    while True:
        jogadas = jogadas + 1
        
        if(jogadas > 9):
            break
        
        jogador1L = int(input("Digite uma linha [1][2][3]: "))
        jogador1C = int(input("Digite uma coluna [1][2][3]: "))

        if(jogador1L == 1 and jogador1C == 1) and tableA[0] != "X" and tableA[0]  != "O":
            tableA[0] = "X"
        if(jogador1L == 1 and jogador1C == 2) and tableA[1] != "X" and tableA[1]  != "O":
            tableA[1] = "X"
        if(jogador1L == 1 and jogador1C == 3) and tableA[2] != "X" and tableA[2]  != "O":
            tableA[2] = "X"


        if(jogador1L == 2 and jogador1C == 1) and tableB[0] != "X" and tableB[0]  != "O":
            tableB[0] = "X"
        if(jogador1L == 2 and jogador1C == 2) and tableB[1] != "X" and tableB[1]  != "O":
            tableB[1] = "X"
        if(jogador1L == 2 and jogador1C == 3) and tableB[2] != "X" and tableB[2]  != "O":
            tableB[2] = "X"

        if(jogador1L == 3 and jogador1C == 1) and tableC[0] != "X" and tableC[0]  != "O":
            tableC[0] = "X"
        if(jogador1L == 3 and jogador1C == 2) and tableC[1] != "X" and tableC[1]  != "O":
            tableC[1] = "X"
        if(jogador1L == 3 and jogador1C == 3) and tableC[2] != "X" and tableC[2]  != "O":
            tableC[2] = "X"
        
        print(tableA)
        print(tableB)
        print(tableC)
        
        if(checavitoria() == 1):
           check_vencedor = 1


        jogadas = jogadas + 1
        if(jogadas > 9):
            break
        jogador2L = int(input("Digite uma linha [1][2][3]: "))
        jogador2C = int(input("Digite uma coluna [1][2][3]: "))

        if(jogador2L == 1 and jogador2C == 1) and tableA[0] != "X" and tableA[0]  != "O":
            tableA[0] = "O"
        if(jogador2L == 1 and jogador2C == 2) and tableA[1] != "X" and tableA[1]  != "O":
            tableA[1] = "O"
        if(jogador2L == 1 and jogador2C == 3) and tableA[2] != "X" and tableA[2]  != "O":
            tableA[2] = "O"


        if(jogador2L == 2 and jogador2C == 1) and tableB[0] != "X" and tableB[0]  != "O":
            tableB[0] = "O"
        if(jogador2L == 2 and jogador2C == 2) and tableB[1] != "X" and tableB[1]  != "O":
            tableB[1] = "O"
        if(jogador2L == 2 and jogador2C == 3) and tableB[2] != "X" and tableB[2]  != "O":
            tableB[2] = "O"

        if(jogador2L == 3 and jogador2C == 1) and tableC[0] != "X" and tableC[0]  != "O":
            tableC[0] = "O"
        if(jogador2L == 3 and jogador2C == 2) and tableC[1] != "X" and tableC[1]  != "O":
            tableC[1] = "O"
        if(jogador2L == 3 and jogador2C == 3) and tableC[2] != "X" and tableC[2]  != "O":
            tableC[2] = "O"

        
        print(tableA)
        print(tableB)
        print(tableC)
        if(checajogador() == 1):
           check_vencedor = 1

    if(jogadas > 9) and (check_vencedor == ''):
            print("DEU VELHA!!")
           

def checavitoria():
        if(tableA[0] == 'X') and (tableA[1] == 'X') and (tableA[2] == 'X'):
                print("Jogador X Ganhou!!")
                return 1
        elif(tableB[0] == 'X') and (tableB[1] == 'X') and (tableB[2] == 'X'):
                print("Jogador X Ganhou!!")
                return 1
        elif(tableC[0] == 'X') and (tableC[1] == 'X') and (tableC[2] == 'X'):
                print("Jogador X Ganhou!!")
                return 1
        elif(tableA[0] == 'X') and (tableB[0] == 'X') and (tableC[0] == 'X'):
                print("Jogador X Ganhou!!")
                return 1
        elif(tableA[1] == 'X') and (tableB[1] == 'X') and (tableC[1] == 'X'):
                print("Jogador X Ganhou!!")
                return 1
        elif(tableA[2] == 'X') and (tableB[2] == 'X') and (tableC[2] == 'X'):
                print("Jogador X Ganhou!!")
                return 1
        elif(tableA[0] == 'X') and (tableB[1] == 'X') and (tableC[2] == 'X'):
                print("Jogador X Ganhou!!")
                return 1
        elif(tableC[0] == 'X') and (tableB[1] == 'X') and (tableA[2] == 'X'):
                print("Jogador X Ganhou!!")
                return 1

def checajogador():
        if(tableA[0] == 'O') and (tableA[1] == 'O') and (tableA[2] == 'O'):
                print("Jogador O Ganhou!!")
                return 1
        elif(tableB[0] == 'O') and (tableB[1] == 'O') and (tableB[2] == 'O'):
                print("Jogador O Ganhou!!")
                return 1
        elif(tableC[0] == 'O') and (tableC[1] == 'O') and (tableC[2] == 'O'):
                print("Jogador O Ganhou!!")
                return 1
        elif(tableA[0] == 'O') and (tableB[0] == 'O') and (tableC[0] == 'O'):
                print("Jogador O Ganhou!!")
                return 1
        elif(tableA[1] == 'O') and (tableB[1] == 'O') and (tableC[1] == 'O'):
                print("Jogador O Ganhou!!")
                return 1
        elif(tableA[2] == 'O') and (tableB[2] == 'O') and (tableC[2] == 'O'):
                print("Jogador O Ganhou!!")
                return 1
        elif(tableA[0] == 'O') and (tableB[1] == 'O') and (tableC[2] == 'O'):
                print("Jogador O Ganhou!!")
                return 1
        elif(tableC[0] == 'O') and (tableB[1] == 'O') and (tableA[2] == 'O'):
                print("Jogador O Ganhou!!")

                return 1


            
            
while True:

    entrada()

    continuar = input('Deseja continuar o jogo [s] [n]?:')
    if(continuar == 's'):
        tableA = ['_','_','_']
        tableB = ['_','_','_']
        tableC = ['_','_','_']
        table = [tableA,tableB,tableC]

    elif(continuar == 'n'):
        break
                      
