'''
Projeto Jogo Pedra-Papel-Tesoura
2024.08.13
Beatriz Costa
'''

# --> Bibliotecas 
# Importa funções do modules.py
from modules import clrScreen, displayLine, displayMsg, displayMsgCenter, displayHeader, getUserOption, validateUserOption # Nesse bloco aqui, estaremos chamando diversas funções para conseguirmos realizar o programa.
from ppt import startPPT # chamamos a função ppt para começarmos a jogar o programa PPT
from parimpar import startParImpar

# --> Constantes, Varáveis e Listas

# --> Funções

# --> Main
msgs = ['Seja Bem vind@ aos Jogos', 'PEDRA-PAPEL-TESOURA', 'PAR OU ÍMPAR']
displayHeader(msgs)
msgs = ['Digite 0 -- Sair', 'Digite 1 -- Pedra-Papel-Tesoura', 'Digite 2 -- Par ou Ímpar']
displayHeader(msgs)
opUser = getUserOption('Sua escolha')
while not validateUserOption(opUser, ['0', '1', '2']):
  opUser = getUserOption('Sua escolha')
if(opUser == '1'):
  startPPT()
elif(opUser == '2'):
  startParImpar()
else:
  displayMsg('Até a proxima...')
startPPT() # Precisaremos para começar o jogo.