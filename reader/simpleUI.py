from pathlib2 import Path
import json
import os
DEFAULT_KEY = "0"
CONFING_PATH = "./config/config.json"
class simpleUI:
    def get_input(self, message, default_value = "-1"):
        valore = input(message)
        if valore == DEFAULT_KEY and default_value != "-1":
            valore = default_value
        return valore

    def clear_console(self):
        os.system("cls")

    def return_to_menu(self):
        input("Premi un tasto per continuare...")
        self.clear_console()
        self.print_menu()
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
            "Inserire il percorso completo, assoluto, della cartella di destinazione delle trascrizioni (indicare una cartella vuota) "
            "\nDEFAULT: './RawTranscript'\n", "./RawTranscript")

        lingua = self.get_input("Scegliere la lingua degli audio su cui si effettuano le trascrizioni:\n"
                                "[1] Multilingua: rilevamento automatico, italiano incluso. La trascrizione è più lenta\n"
                                "[2] Inglese: specifico per la lingua, più precisa e veloce per quest'ultima\n "
                                "DEFAULT: Multilingua\n", "1")
        lingua = int(lingua)

        modello = self.get_input("Scegliere il modello AI da utilizzare per le trascrizioni, più un modello è potente più è preciso e più richiede risorse\n"
                                 "La tabella è un estratto dalla pagina di OpenAI di Whisper, l'ultima colonna indica quanto velocemente l'AI 'riproduce' l'audio\n."
                                 "      | Size   | Required VRAM | Relative speed\n"
                                 "  [1] | tiny   |     ~1 GB     |      ~32x\n"
                                 "  [2] | base   |     ~1 GB     |      ~16x\n"
                                 "  [3] | small  |     ~2 GB     |      ~6x\n"
                                 "  [4] | medium |     ~5 GB     |      ~2x\n"
                                 "  [5] | large  |     ~10 GB    |      ~1x\n"
                                 "DEFAULT: base\n", "2")
        modello = int(modello)
        ask_prompt = self.get_input(
            "Il modello di intelligenza artificiale può utilizzare una breve frase (scritta in inglese) che descriva "
            "il contenuto dell'audio per migliorare la sua precisione. Tuttavia tale inserimento è falcoltativo, "
            "vuoi che ad ogni comando di trascrizione ti venga richiesto di inserire questa frase? [y/n]\n"
            "DEFAULT: SI\n", "y")
        if ask_prompt == "y":
            ask_prompt = True
        else:
            ask_prompt = False


        config = {}
        config["booted"] = True
        config["audio_path"] = audio_path
        config["dest_path"] = dest_path
        config["lingua"] = lingua
        config["modello"] = modello
        config["ask_prompt"] = ask_prompt

        with open(CONFING_PATH, "w") as outfile:
            json.dump(config, outfile)

        print("Configurazione completata con successo!")
        input("Premi un tasto per continuare...")
        self.clear_console()
        self.print_menu()

    def print_menu(self):
        print("-------------------------STUDENT COPILOT----------------------------\n"
              "Scegli cosa vuoi fare premendo il tasto tra le parentesi quadre\n"
              "[1] Converti un file audio in file word\n"
              "[2] Converti tutti i file presenti nella cartella in un unico file word\n"
              "[3] Converti ogni file presente nella cartella nel suo corrispettivo file word\n"
              "[4] Opzioni\n"
              "[5] Esci\n")


