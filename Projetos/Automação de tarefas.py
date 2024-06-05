# Auxiliar.py para posicionamento dos cliques do mouse:

import pyautogui
import time

time.sleep(6) 
print(pyautogui.position()) 


# codigo.py

import pyautogui
import time

pyautogui.PAUSE = 0.5
pyautogui.press('win') 
pyautogui.write('chorme') 
pyautogui.press('enter')

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
  
time.sleep(2)

pyautogui.click(x=656, y=411)
pyautogui.write('pythonimpressionador@gmail.com') 

pyautogui.press('tab') 
pyautogui.write('sua senha')

pyautogui.press('tab')
pyautogui.press('enter')

import pandas as pd

tabela = pd.read_csv('produtos.csv') 
print(tabela)

pyautogui.press('enter')

for linha in tabela.index: 

    pyautogui.click(x=645, y=294)

    codigo = str(tabela.loc[linha, 'codigo'])

    pyautogui.write(codigo)
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'categoria'])) 
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    obs = (tabela.loc[linha, 'obs'])
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
        
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000) 
