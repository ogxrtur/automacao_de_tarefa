# passo 1: entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# passo 2: Fazer login
# passo 3: importar a base de dados
# passo 4: Cadastrar 1 produto
# passo 5: repetir para todos os produtos

import pyautogui
import time 
import pandas



pyautogui.PAUSE = 0.5


pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=725, y=357)
pyautogui.write("arturv827@gmail.com")
pyautogui.click(x=715, y=449)
pyautogui.write("python2425")
pyautogui.press("enter")

time.sleep(3)

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    pyautogui.click(x=698, y=251)

    codigo = tabela.loc [linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc [linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc [linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc [linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc [linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc [linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc [linha, "obs"])
    if obs != "nan":
         pyautogui.write(obs)  

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(100000)


