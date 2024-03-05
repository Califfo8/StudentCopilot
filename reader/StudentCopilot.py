import whisper
import docx
import json
from pathlib2 import Path
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer
# from gensim.summarization import summarize
# from transformers import BartTokenizer, BartForConditionalGeneration
# from summarizer import Summarizer
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
# import nltk
# import openai
class StudentCopilot:
    def __init__(self, config_path):
        f = open(config_path + 'config.json')
        data = json.load(f)
        f.close()
        self.audio_path = data['audio_path'] + "/"
        self.transcriptin_path = data['dest_path']+ "/"
        self.lingua = data['lingua']
    def createWordFile(self, FILE_NAME, text):
        print("Exporting in microsoft word...")
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
        print("Operazione conclusa con successo!")

    def summarizeText(self, text):
        # model = Summarizer()

        # Decode and output the summary
        # summary = model(text)
        print("\nSummary:")
        # print(summary)

    def convertSpeechToText_OpenAI(self, file_name, prompt=""):
            FILE_PATH = self.audio_path + file_name

            print("Loading model...")
            if self.lingua == 2:
                model = whisper.load_model("base.en")
            elif self.lingua == 1:
                model = whisper.load_model("base")
            else:
                print("ERRORE: La lingua impostata non è valida")
                return

            print("Starting transcription...")
            result = model.transcribe(FILE_PATH, verbose=True, fp16=False, initial_prompt=prompt)

            self.createWordFile(file_name, result['text'])

    def convertAllSpeechToText(self, prompt=""):
        elements = os.listdir(self.audio_path)
        only_files = []
        print("I seguenti file verranno trascritti:")
        for f in elements:
            path = Path(self.audio_path + f)
            if path.is_file():
                only_files.append(f)
                print("\t - " + f)
        risp = input("Vuoi continuare? [y/n]")
        if risp == 'n':
            return
        print("Loading model...")
        if self.lingua == 2:
            model = whisper.load_model("base.en")
        elif self.lingua == 1:
            model = whisper.load_model("base")
        else:
            print("ERRORE: La lingua impostata non è valida")
            return

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