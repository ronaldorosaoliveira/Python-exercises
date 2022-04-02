# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
partidas = []
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do jogador: "))
    tot = int(input(f"Quantas partidas o {jogador['nome']} jogou? "))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols na {c+1}ª partida? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        continua = str(input('Quer continuar [S/N] ? ')).upper()
        if continua in "SN":
            break
        print('Erro. Responda apenas S ou N')
    if continua in "N":
        break
print('-=' *30)
print('cod ', end="")
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print("--" * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print("-" * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador ? (999 para finalizar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro. Não existe jogador com o código {busca}')
    else:
        print(f' -- Levantamento do Jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i+1}, fez {g} gols')
    print("-" * 30)
print("<<< VOLTE SEMPRE >>>")