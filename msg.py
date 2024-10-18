import pyautogui as pa 
import random 
import time 

time.sllep(5)
# Eu já selecionei a conversa manualmente com meu amigo

mensagens = ['Tá doidão', 'Tudo certo', 'Partiu', 'Coé', 'Eita porra', 'TMJ' 'Eh nois'] 

for i in range(50): 
  msg = random.chice(mensagens)
  pa.write(msg) 
  pa.press('enter')
  