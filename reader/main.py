from reader.StudentCopilot import StudentCopilot
from reader.simpleUI import simpleUI
CONFING_PATH = "./appdata/config/"
PROMPT_PHRASE = ("Inserire una breve frase in Inglese che descriva il contenuto dell'audio, o degli audio nel loro\n"
                 "insieme, da trascrivere (es: 'Lesson about the application of neural networks in the field of AI'),\n"
                 "può essere lasciato vuoto:")
# Press the green button in the gutter to run the script.
def main():
    sUI = simpleUI()
    sUI.bootstrap()

    SC = StudentCopilot(CONFING_PATH)
    command = -1
    while command != 5:
        command = int(input())
        prompt = ""
        if command == 1:
            file_name = input("Inserire il nome del file, estenzione inclusa (es: lezione1.m4a): ")
            if SC.prompt:
                prompt = input(PROMPT_PHRASE)
            SC.convert_speech_to_text_openai(file_name, prompt)
            sUI.return_to_menu()
        elif command == 2:
            if SC.prompt:
                prompt = input(PROMPT_PHRASE)
            SC.convert_all_speech_to_text(prompt)
            sUI.return_to_menu()
        elif command == 3:
            if SC.prompt:
                prompt = input(PROMPT_PHRASE)
            SC.convert_all_to_many(prompt)
            sUI.return_to_menu()
        elif command == 4:
            SC.options()
            sUI.return_to_menu()