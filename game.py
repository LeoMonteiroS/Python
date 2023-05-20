from random import choice # importando modulo "arquivo" random.  Importando somente a funcao choice

vitorias_jogador = 0
vitorias_maquina = 0

def Opcao_jogador():
    esc_jogador = input("Esolha: Pedra, Papel ou Tesoura ")
    esc_jogador.lower()
    if esc_jogador == "pedra":
        return esc_jogador
    elif esc_jogador == "tesoura":
        return esc_jogador
    elif esc_jogador == "papel":
        return esc_jogador
    else:
        print("Digite uma opcao valida. Tente novamente")
        Opcao_jogador()


def Opcao_maquina():
    esc_maquina =  choice(["pedra", "papel", "tesoura"])
    return esc_maquina


while True:
    
    print("-"*10)    
    esc_jogador = Opcao_jogador()
    esc_maquina = Opcao_maquina()
    print("-"*30)
    
    if (esc_jogador == "pedra") and (esc_maquina == "tesoura") \
        or (esc_jogador == "papel") and (esc_maquina == "pedra") \
            or (esc_jogador == "tesoura") and (esc_maquina == "papel"):
                #jogador ganha
                print(f"Voce escolheu {esc_jogador} e a Maquina escolheu {esc_maquina}."
                      " Resultado: Voce Gahou !") #ligando as strings pq n pode na mesmo linha
                vitorias_jogador += 1
    #empate
    elif esc_jogador == esc_maquina:
        print(f"Voce escolheu {esc_jogador} e a Maquina escolheu {esc_maquina}."
                      " Resultado: Empate !")
     #jogador perdeu   
    else:
        print(f"Voce escolheu {esc_jogador} e a Maquina escolheu {esc_maquina}."
              " Resultado: Voce Perdeu !") #ligando as strings pq n pode na mesmo linha
        vitorias_maquina += 1
        
    print("-"*30)
    print(f"Vitorias do jogador {vitorias_jogador}")
    print(f"Vitorias da maquina {vitorias_maquina}")
    print("-"*30)
    
    esc_jogador = input("Voce quer continuar jogando ? ")
    if esc_jogador in ["Sim", "SIM", "sim", "S", "s"]:
        pass
    elif esc_jogador in ["Nao", "nao", "NAO", "N", "n"]:
        break
    else:
        break