# pip install pyautogui
import pyautogui
import time
import pandas as pd

pyautogui.PAUSE=0.5

pyautogui.press('win')
pyautogui.write('Edge')
pyautogui.press('enter')
pyautogui.hotkey('Alt','space')
pyautogui.press('x')
time.sleep(0.3)
pyautogui.hotkey('Ctrl','l')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
pyautogui.click(x=2543, y=482)
pyautogui.write('marcesouza@gmail.com')
pyautogui.click(x=2532, y=611)
pyautogui.write('1234')
pyautogui.press('tab')
pyautogui.press('enter')


tabela=pd.read_csv('produtos.csv')

for i in tabela.index:

    pyautogui.click(x=2547, y=345)
    codigo=tabela.loc[i,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    marca=tabela.loc[i,"marca"]
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    tipo=tabela.loc[i,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    categoria=tabela.loc[i,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    preco_unitario=tabela.loc[i,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    custo=tabela.loc[i,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    obs=tabela.loc[i,"obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.hotkey('Ctrl','Home')
 