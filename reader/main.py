from reader.StudentCopilot import StudentCopilot
from reader.simpleUI import simpleUI
CONFING_PATH = "./config/"
# Press the green button in the gutter to run the script.
def main():
    sUI = simpleUI()
    sUI.bootstrap()

    SC = StudentCopilot(CONFING_PATH)
    command = -1
    while command != 4:
        command = int(input())
        if command == 1:
            file_name = input("Inserire il nome del file, estenzione inclusa (es: lezione1.m4a): ")
            prompt = input("Inserire una breve frase che descriva il contenuto dell'audio (es: 'Lezione di storia "
                           "riguardante la prima guerra mondiale'), può essere lasciato vuoto: ")
            SC.convertSpeechToText_OpenAI(file_name, prompt)
            sUI.returnToMenu()
        elif command == 2:
            prompt = input("Inserire una breve frase che descriva il contenuto degli audio (es: 'Lezione di storia "
                           "riguardante la prima guerra mondiale'), può essere lasciato vuoto: ")
            SC.convertAllSpeechToText()
            sUI.returnToMenu()
        elif command == 3:
            prompt = input("Inserire una breve frase che descriva il contenuto degli audio (es: 'Lezione di storia "
                           "riguardante la prima guerra mondiale'), può essere lasciato vuoto: ")
            SC.convertAllToMany(prompt)
            sUI.returnToMenu()