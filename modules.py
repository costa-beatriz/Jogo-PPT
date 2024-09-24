'''
Arquivo de Modulos
2024.08.13
Beatriz Costa
'''

# --> Bibliotecas
from random import choice 
from time import sleep

# --> Constantes, Varáveis e Listas
TAM = 50 # Tamanho da Tela
CAR = choice(['=', '*', '|', '-']) # Caracter utilizado para desenho da tela
MAR = 4 # Tamanho da Margem

# --> Funções
def clrScreen(): # Função para limpar a tela
  print('\n'*TAM) # Mostra na tela \n == linha * TAM

def displayLine(): # Função para mostrar uma linha de caracteres  
  print(CAR*TAM) # Mostra na tela o caractere (=, *, |, -) "vezes" o tamanho da tela

def displayMsg(msg): # Mostra uma mensagem alinhada a esquerda entre CAR
  print(f'{CAR} {msg:<{TAM-MAR}} {CAR}') # Mostra na tela, os caracteres(que forma uma tela), com a mensagem no canto esquerdo, < o tamanho da margem.

def displayMsgCenter(msg): # Função para mostrar mensagem no centro da tela
  print(f'{CAR} {msg:^{TAM-MAR}} {CAR}') # Mostra a mensagem ao centro, junto com os caracteres, centralizando o tamanho da tela e da margem(centralizando a mensagem tbm)

def displayHeader(msgs): # Função do cabeçalho 
  displayLine() # Mostra a linha
  for item in msgs: # Função para as mensagens
    displayMsgCenter(item) # 
  displayLine()

def displayHeaderT(msgs):  
  displayLine() 
  for item in msgs: 
    displayMsgCenter(item) 
    sleep(1)
  displayLine()

def getUserOption(msg):
  option = input(f'{CAR} {msg}: ').strip()
  return option
  
def validateUserOption(option, listOptions): # Função para verificar se as respostas se sao falsas ou verdadeiras(se for colocado as respostas certas ou nao)
  if option in listOptions: 
    return True
  else: # Se for falso
    msgsErro = ['Opção Inválida', 'Escolha Novamente...'] # Ira aparecer essa mensagem
    displayHeader(msgsErro) # Verificando se for qualaquer outro carectere, e nao o desejado.
    return False # Confirma se é falso

# --> Main