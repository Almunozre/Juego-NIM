


def usuario_escolhe_jogada(n, m):
    jugada = 0
    while jugada < 1 or jugada > m or jugada > n:
        jugada = int(input("Quantas peças você vai tirar? "))
        print()
        if jugada < 1 or jugada > m or jugada > n:
            print("Oops! Jogada inválida! Tente de novo.")
            print()
    return jugada
        
    
def computador_escolhe_jogada(n, m):
    if n % (m + 1) != 0:
        return n % (m+1)
    else:
        return m



def partida():
    
    n = int(input("Quantas pecas?: "))
    m = int(input("limite de pecas por jogada?: "))
    print()
    
    if n < m:
        print("jugada invalida")
        partida()
    elif n % (m + 1) == 0:
        print("Voce começa!")
       
        print()
        turno_usuario = True
    else:
        print("Computador começa!")
        print()
        turno_usuario = False
    
    
    while n > 0:
        if turno_usuario:
            jugada_usuario = usuario_escolhe_jogada(n, m)
            print(f"voce tirou {jugada_usuario} pecas")
            print()
            n = n - jugada_usuario
            turno_usuario = False
        else:
            jugada_computador = computador_escolhe_jogada(n, m)
            print(f"O computador tirou {jugada_computador} peca")
            print()
            n -= jugada_computador
            turno_usuario = True
        
        print(f"Agora restam {n} peças no tabuleiro")
   
    if turno_usuario:
        print("\nFim do jogo! O computador ganhou!")
    else:
        print("\nFim do jogo! Você ganhou!")

def campeonato():
    
    Computador = 0
    Voce = 0
    
    for _ in range (3): 
        print(f"\n**** Rodada {_ + 1 } ***\n")
        resultado = partida()
        if resultado == "Você ganhou!":
            Voce += 1
        else:
            Computador += 1
            
    print("\n**** Final do campeonato! ****") 

    print(f"\nPlacar: Você {Voce} X {Computador} Computador")   


print("\nBem-vindo ao jogo do NIM! Escolha:\n")
    
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato 2 \n")
    
opcion = int(input("Ingrese la opcion: "))
    
if opcion == 1:
    print("\nVoce escolheu uma partida!\n")
    partida()
elif opcion == 2:
    print("Voce escolheu um campeonato!")  
    campeonato()
         
    
