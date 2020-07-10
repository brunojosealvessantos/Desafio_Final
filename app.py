import pyautogui
import webbrowser
import time


class Bot:
    def __init__(self):
        webbrowser.open('https://cursoautomacao.netlify.app/')
        time.sleep(2)

    def escreverNome(self):
        pyautogui.moveTo(x=400, y=400)
        pyautogui.scroll(-1000)
        pyautogui.click(x=979, y=197)
        pyautogui.write('Bruno')

    def printScreen(self):
        pyautogui.screenshot('foto.jpg', region=(
            900, 127, (1325-900), (268-127)))

    def radioButtonMarc(self):
        pyautogui.scroll(1000)
        pyautogui.click(x=42, y=282)

    def downloadArquivos(self):
        listaPosicaoArquivos = [(181, 549), (380, 551), (540, 554),
                                (760, 588), (979, 556), (1098, 585)]
        pyautogui.scroll(-1700)
        for posicao in listaPosicaoArquivos:
            pyautogui.click(posicao)


bot = Bot()
bot.escreverNome()
bot.printScreen()
bot.radioButtonMarc()
bot.downloadArquivos()
