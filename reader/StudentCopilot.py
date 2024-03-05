import whisper
import docx
import json
from pathlib2 import Path
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

class StudentCopilot:
    def __init__(self, config_path):
        f = open(config_path + 'config.json')
        data = json.load(f)
        f.close()
        self.audio_path = data['audio_path'] + "/"
        self.transcriptin_path = data['dest_path']+ "/"
        self.lingua = data['lingua']
    def get_model(self):
        if self.lingua == 2:
            return whisper.load_model("base.en")
        elif self.lingua == 1:
            return whisper.load_model("base")
        else:
            print("ERRORE: La lingua impostata non è valida")
            return None
    def createWordFile(self, FILE_NAME, text, save=True):
        print("Esportando in microsoft word...")
        title = FILE_NAME[0:FILE_NAME.find('.')]
        # Create a document
        doc = docx.Document()
        # Add a paragraph to the document
        p = doc.add_paragraph()
        # Add a run to the paragraph
        run = p.add_run(title)
        p.style = doc.styles['Heading 2']
        # Add another paragraph
        p = doc.add_paragraph()
        p.style = doc.styles['Normal']
        # Add a run and format it
        run = p.add_run(text)
        # Save the document
        doc.save(self.transcriptin_path + title + ".docx")
        print("Trascritto file " + FILE_NAME + " con successo!")

    def convertSpeechToText_OpenAI(self, file_name, prompt=""):
            FILE_PATH = self.audio_path + file_name

            print("Loading model...")
            model = self.get_model()
            print("Starting transcription...")
            result = model.transcribe(FILE_PATH, verbose=True, fp16=False, initial_prompt=prompt)

            self.createWordFile(file_name, result['text'])
    def get_all_files(self):
        elements = os.listdir(self.audio_path)
        only_files = []
        for f in elements:
            path = Path(self.audio_path + f)
            if path.is_file():
                only_files.append(f)
        return only_files
    def askForConfirmation(self, only_files):
        print("I seguenti file verranno trascritti:")
        for f in only_files:
            print("\t - " + f)
        risp = input("Vuoi continuare? [y/n]")
        while risp != 'y' and risp != 'n':
            risp = input("Vuoi continuare? [y/n]")
        if risp == 'n':
            return False
        return True

    def convertAllSpeechToText(self, prompt=""):
        only_files = self.get_all_files()
        if not self.askForConfirmation(only_files):
            return

        print("Loading model...")
        model = self.get_model()
        print("Starting transcription...")
        doc = docx.Document()
        for f in only_files:
            file_path = self.audio_path + f
            result = model.transcribe(file_path, verbose=False, fp16=False, initial_prompt=prompt)
            title = f[0:f.find('.')]
            # Add a paragraph to the document
            p = doc.add_paragraph()
            # Add a run to the paragraph
            run = p.add_run(title)
            p.style = doc.styles['Heading 2']
            # Add another paragraph
            p = doc.add_paragraph()
            p.style = doc.styles['Normal']
            # Add a run and format it
            run = p.add_run(result['text'])
            print("Trascritto " + f)
        # Save the document
        doc.save(self.transcriptin_path + "Trascrizioni.docx")
        print("Operazione conclusa con successo!")

    def convertAllToMany(self, prompt=""):
        only_files = self.get_all_files()
        if not self.askForConfirmation(only_files):
            return

        print("Loading model...")
        model = self.get_model()
        print("Starting transcription...")
        doc = docx.Document()
        for f in only_files:
            file_path = self.audio_path + f
            result = model.transcribe(file_path, verbose=False, fp16=False, initial_prompt=prompt)
            self.createWordFile(f, result['text'])
        print("Tutti i file sono stati trascritti correttamente!")