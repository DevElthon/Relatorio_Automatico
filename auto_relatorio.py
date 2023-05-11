import pyautogui
import time
import pandas as pd
import pyperclip
import datetime

#controle de quando o programa será rodado
dias_da_semana=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
today = datetime.date.today()
semana_num=today.weekday()
print(dias_da_semana[semana_num])

if dias_da_semana[semana_num] == "Friday":
    #Tratamento de dados
    tabela = pd.read_csv("Compras.csv", sep=";")

    print(tabela)
    total_gasto = tabela["ValorFinal"].sum()
    quantidade = tabela["Quantidade"].sum()
    preco_medio = total_gasto/quantidade

    print(f"Total gasto: {total_gasto}")
    print(f"Quantidade: {quantidade}")
    print(f"Preco medio: {preco_medio}")

    #Envio de relatorio por email
    pyautogui.PAUSE = 2

    pyautogui.click(x=207, y=1053)
    pyautogui.write("chrome")
    pyautogui.press("enter")

    time.sleep(2)

    pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
    pyautogui.press("enter")

    time.sleep(5)

    pyautogui.click(x=171, y=248)
    pyautogui.write("elthonarcaan@gmail.com")
    pyautogui.press("enter")

    pyautogui.press("tab")
    pyperclip.copy("Relatório de Vendas")
    pyautogui.hotkey("ctrl", "v")

    pyautogui.press("tab")
    texto = f""" Bom dia,
    Segue o relatório de compras.

    Total Gasto: R${total_gasto:,.2f}
    Quantidade de Produtos: R${quantidade:,.2f}
    Preço Médio: R${preco_medio:,.2f}

    Qualquer dúvida, entre em contato.
    Att., Elthon.
    """

    pyperclip.copy(texto)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("ctrl", "enter")