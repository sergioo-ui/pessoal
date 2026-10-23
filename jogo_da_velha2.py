# Inicializa o tabuleiro com números de 1 a 9 para facilitar as jogadas
tabuleiro = [str(i) for i in range(1, 10)]

def mostrar_tabuleiro():
    print("\n")
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---|---|---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---|---|---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print("\n")

def verificar_vitoria(jogador):
    # Combinações possíveis para vencer
    vitorias = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Colunas
        [0, 4, 8], [2, 4, 6]            # Diagonais
    ]
    for condicao in vitorias:
        if tabuleiro[condicao[0]] == tabuleiro[condicao[1]] == tabuleiro[condicao[2]] == jogador:
            return True
    return False

def jogar():
    jogador_atual = "X"
    jogadas = 0

    while jogadas < 9:
        mostrar_tabuleiro()
        try:
            escolha = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1
            
            # Valida se a jogada está dentro do limite e se a casa está livre
            if 0 <= escolha < 9 and tabuleiro[escolha] not in ["X", "O"]:
                tabuleiro[escolha] = jogador_atual
                jogadas += 1

                if verificar_vitoria(jogador_atual):
                    mostrar_tabuleiro()
                    print(f"Parabéns! O Jogador {jogador_atual} venceu!")
                    return
                
                # Alterna o jogador
                jogador_atual = "O" if jogador_atual == "X" else "X"
            else:
                print("Jogada inválida! Escolha uma posição vazia entre 1 e 9.")
        except ValueError:
            print("Por favor, digite apenas números inteiros de 1 a 9.")

    mostrar_tabuleiro()
    print("Empate!")

# Executa o jogo
if __name__ == "__main__":
    jogar()