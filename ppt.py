'''
Jogo do Pedra-Papel-Tesoura
2024.08.13
Beatriz costa
'''

# Bibliotecas
from modules import clrScreen, displayHeader, getUserOption, validateUserOption, displayLine, displayMsg, displayMsgCenter, displayHeaderT # Funções importadas para funcionar o código.
from random import randint # Sortear um numero aleatorio inteiro
from time import sleep

# Constantes, Variaveis e Listas
msgsInicio = ['Seja bem vind@ ao', 'Jogo do PEDRA-PAPEL-TESOURA', 'desenvolvido por: Beatriz Costa', 'BOA SORTE'] # Mensagem que aparece ao inicio do jogo, informando o nome do jogo, o autor e uma mensagem de boa sorte.
msgs = []
playAgain = '' # Caractere usado para jogarmos de novo.
playerScore = 0
computerScore = 0

# Funções
def startPPT(): # 
  while(True): # Verificar se sempre é verdade
    clrScreen() # Limpar a tela
    displayHeader(msgsInicio) # Cabeçalho das mensagens apos o caracteres que formam a tela.
    # função para começar o jogo
    playPPT()
    playAgain = getUserOption('Deseja jogar novamente [s/n]') # Mensagem que aparecera para você jogar novamente
    while not validateUserOption(playAgain, ['s', 'n', 'S', 'N',]): # Opções que iram aparecer se vc desejar jogar novamente.
      playAgain = getUserOption('Deseja jogar novamente [s/n]') # Opção para jogar novamente.
    if playAgain.lower() != 's': # Se a resposta for's' o jogo irá parar.
      break

def displayMenu():
  msgs = ['Escolha:', ]
  displayLine()
  for msg in msgs:
    displayMsg(msg)
  displayLine()


  
def displayScore(typeScore, playerScore, computerScore):
  msgs = []
  msgs.append(typeScore)
  msgs.append (f'Player: {playerScore} --- PC: {computerScore}')
  displayHeaderT(msgs)

def determineWinner(playerChoice, computerChoice):
  play = ''
  result = ''
  choices = ['PEDRA', 'PAPEL', 'TESOURA']
  playerChoiceStr = choices[int(playerChoice)]
  computerChoiceStr = choices[int(computerChoice)]
  if playerChoice == computerChoice:
    result = 'Empate!'
  elif (playerChoice == '0' and computerChoice == '2') or \
       (playerChoice == '1' and computerChoice == '0') or \
       (playerChoice == '2' and computerChoice == '1'):
    play = f'{playerChoiceStr} vence {computerChoiceStr}'
    result = 'Você Ganhou!'
  else:
    play = f'{computerChoiceStr} vence {playerChoiceStr}'
    result = 'Você Perdeu!'
  msgs = ['Jogada do Player: ' + playerChoiceStr, 'Jogada do PC: ' + computerChoiceStr, play, result]
  displayHeaderT(msgs)
  return result

def playPPT():
  playerScore = 0 
  computerScore = 0
  while playerScore < 2 and computerScore < 2:
    displayMenu()
    playerChoice = getUserOption('Sua escolha')
    while not validateUserOption(playerChoice, ['0', '1', '2']):
      displayMenu()
      playerChoice = getUserOption('Sua escolha')
    computerChoice = str(randint(0,2))
    result = determineWinner(playerChoice, computerChoice)
    if 'Ganhou' in result:
      playerScore += 1
    elif 'Perdeu' in result:
      computerScore += 1 
    if playerScore < 2 and computerScore < 2:
      displayScore('PLACAR', playerScore, computerScore)
    sleep(1)
  displayScore('PLACAR FINAL', playerScore, computerScore)
  if playerScore > computerScore:
    displayHeader(['Parabéns','YOU WIN!'])
  else:
    displayHeader(['Parabéns', 'YOU LOSE!'])
    
# Main