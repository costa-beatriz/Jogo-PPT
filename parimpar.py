'''
Jogo do Ímpar ou Par
2024.08.20
Beatriz Costa
'''

# Bibliotecas
from modules import clrScreen, displayHeader, getUserOption, validateUserOption, displayLine, displayMsg, displayMsgCenter, displayHeaderT # Códigos para importarmos
from random import randint # Importa numeros inteiros aleatorios
from time import sleep # Importa o tempo para que o código vá descendo na tela

# Constantes, Variáveis e Listas
msgsInicio = ['Seja Bem Vindo ao',
              'Jogo do ÍMPAR OU PAR',
              'desenvolvido por: BEATRIZ COSTA',
              'BOA SORTE!'] # Mensagem que aparecera no inicio do jogo
playAgain = '' # Variavel para jogarmos de novo
playerScore = 0 # Variavel do player(pontuação)
computerScore = 0 # Variavel do computador (pontuação)

# Funções
def startParImpar(): # Função para iniciar o jogo
    while(True): # Enquanto for verdade
        clrScreen() # Limpe a tela
        displayHeader(msgsInicio) # Mensagem do inicio do jogo
        playParImpar() # Começa o jogo do Par ou Impar
        playAgain = getUserOption('Deseja jogar novamente [s/n]') # Para jogar de novo, irá aparecer essa mensagem
        while not validateUserOption(playAgain, ['s', 'n', 'S', 'N']): # Se não quiser, você deve apertar essas letras
            playAgain = getUserOption('Deseja jogar novamente [s/n]') # Se não
        if playAgain.lower() != 's': # Deve apertar a letra 's'
            break # Quebra a repetição do código.

def displayMenu(): # Como irá aparecer na tela
    msgs = ['Escolha sua opção:', '[0] --> Ímpar', '[1] --> Par'] # Aparecera para você escolher impar ou par
    displayLine() # Linhas de caracteres
    for msg in msgs: # Enquanto mensagens estiverem dentro de mensagens
        displayMsg(msg) # Para aparecer as mensagens
    displayLine() # Aparece as linhas 

def displayScore(typeScore, playerScore, computerScore): # Função para armazenar os dados do player, e do computador
    msgs = [] # Mensagens do codigo
    msgs.append(typeScore) # Adiciona uma mensagem para lista
    msgs.append(f'Player: {playerScore} --- PC: {computerScore}') # Adiociona mensagem do dado do player, e do computador
    displayHeaderT(msgs) 

def determineWinner(playerChoice, playerNumero, computerNumero): # Determinar o ganhador, definindo as escolhas com os numeros
    play = '' # Variavel para jogar
    result = '' # Variavel para o resultado
    choices = ['ÍMPAR', 'PAR'] # Escolha para impar ou par
    playerChoiceStr = choices[int(playerChoice)] # Escolha do player em texto, mais a escolha de numero inteiro com a escolha do player

    total = playerNumero + computerNumero # Total da resposta do player e do computador
    resultado = 'PAR' if total % 2 == 0 else 'ÍMPAR' # Ira calcular o valor se sao impar ou par

    if resultado.lower() == playerChoiceStr.lower():
        result = 'Você Ganhou' # Resultado se voce ganhar
    else:
        result = 'Você Perdeu' # Resultado se voce perder

    msgs = [f'Sua escolha: {playerChoiceStr}', # Armazena a escolha do player em forma de texto
            f'Seu número: {playerNumero}', # Armazena a escolha do player em forma de numero
            f'Número do PC: {computerNumero}', # Armazena o numero do computador
            f'Total: {total} ({resultado})', # Total + resultado
            result] # Resultado 
    displayHeaderT(msgs)
    return result # Retorna o resultado

def playParImpar(): #começa o jogo
    playerScore = 0 # Pontuação do player
    computerScore = 0 # Pontuação do computador
    while playerScore < 2 and computerScore < 2: # Enquanto a pontuação do jogador e do computador for menor que 2 
        displayMenu() # Mostra o display do menu
        playerChoice = getUserOption('Sua escolha ') # A escolha do player
        while not validateUserOption(playerChoice, ['0', '1']): # Valida se a opção for 0 ou 1 
            displayMenu() # Mostra o display do menu
            playerChoice = getUserOption('Sua escolha') # Irá aparecer essa mensagem para o player escolher

        playerNumero = int(getUserOption('Escolha um número de 0 a 10: ')) # Aparece a mensagem para o player escolher um numero de 0 a 10
        computerNumero = randint(0, 10) # O computador escolhe um numero de 0 a 10

        result = determineWinner(playerChoice, playerNumero, computerNumero) # Resultado para determinar quem irá ficar com ponto, tendo a escolha do player, do numero do player e do numero do computador

        if 'Ganhou' in result: # Se ganhou 
            playerScore += 1 # O player recebe + 1 ponto
        elif 'Perdeu' in result: # Se o player perder
            computerScore += 1 # O computador recebe + 1 ponto

        if playerScore < 2 and computerScore < 2: # Se os dados do player e do computador forem menor que dois irá aparecer o placar
            displayScore('PLACAR', playerScore, computerScore) # Placar dos dados do player e do computador conforme escolhido
        sleep(1) # Espera um segundo para descer a tela

    displayScore('PLACAR FINAL', playerScore, computerScore) # O placar final, com os dados do player e do computador.
    if playerScore > computerScore: # Se os dados do player forem maior que os dados do computador aparecera essas mensagens
        displayHeader(['Parabéns', 'YOU WIN!']) # Mensagem que aparecera se você ganhar.
    else: # Se não
        displayHeader(['Parabéns', 'YOU LOSE!']) # Mensagem que aparecera se você perder.

# Main