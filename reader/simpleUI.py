from pathlib2 import Path
import json
import os
DEFAULT_KEY = "0"
CONFING_PATH = "./config/config.json"
class simpleUI:
    def get_input(self, message, default_value = -1):
        valore = input(message)
        if valore == DEFAULT_KEY and default_value != -1:
            valore = default_value
        return valore

    def clearConsole(self):
        os.system("cls")
    def bootstrap(self):
        config_path = Path(CONFING_PATH)
        if config_path.is_file():
            self.print_menu()
            return

        # creazione delle cartelle necessarie
        os.makedirs("./config", exist_ok=True)
        os.makedirs("./files", exist_ok=True)
        os.makedirs("./RawTranscript", exist_ok=True)

        print("-----------------FIRST CONFIGURATION-----------------")
        print("Benvenuto in StudentCopilot! Prima di iniziare, è necessario configurare il programma. Premere "+ str(DEFAULT_KEY) +" per "
              "inserire il valore di default. Sarà possibile successivamente modificare i valori")

        audio_path = self.get_input(
            "Inserire il percorso completo, assoluto, della cartella dei file audio (selezionare una cartella avente soltanto i file audio "
            "e nessuna sottocartella):\nDEFAULT: './files'\n", "./files")
        dest_path = self.get_input(
            "Inserire il percorso completo, assoluto, della cartella di destionazione delle trascrizioni (indicare una cartella vuota) "
            "\nDEFAULT: './RawTranscript'\n", "./RawTranscript")

        lingua = self.get_input("Scegliere a lingua su cui si effettuano le trascrizioni:\n"
                                "[1] Italiano\n"
                                "[2] Inglese\n")
        lingua = int(lingua)

        config = {}
        config["booted"] = True
        config["audio_path"] = audio_path
        config["dest_path"] = dest_path
        config["lingua"] = lingua
        with open(CONFING_PATH, "w") as outfile:
            json.dump(config, outfile)

        print("Configurazione completata con successo!")
        input("Premi un tasto per continuare...")
        self.clearConsole()
        self.print_menu()

    def print_menu(self):
        print("-----------------MENU-----------------\n"
              "Scegli cosa vuoi fare premendo il tasto tra le parentesi quadre\n"
              "[1] Converti un file audio in file word\n"
              "[2] Converti tutti i file presenti nella cartella audio\n"
              "[3] Esci\n")


