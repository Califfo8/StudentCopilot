# StudentCopilot
StudentCopilot trascrive automaticamente dei file audio in file word, applicando una formattazione semplice al testo generato. La trascrizione si basa su 
[Whisper](https://github.com/openai/whisper?tab=readme-ov-file) di OpenAI.
In questa repository è presente il codice del programma, a destra è possibile scaricare la release per il solo utilizzo. 
## Installazione
### FFmpeg
Il programma richiede lo strumento da riga di comando [FFmpeg](https://ffmpeg.org/download.html#build-windows) installato sul proprio sistema operativo; i file neccessari all'installazione sono recuperabili dal [sito](https://ffmpeg.org/download.html#build-windows) oppure attraverso il download diretto della versione usata per programmare StudentCopilot (Windows Build 2024-03-10 12:52) cliccando [qui](https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl-shared.zip). Il programma funziona anche con le versioni successive.

Di seguito la procedura di installazione dello strumento con anesso l'inserimento del percorso "C:\ffmpeg\bin" nelle proprie variabili di sistema, tale operazione è necessaria al funzionamento di FFmpeg:
1. **Locazione della cartella**:
   - Decomprimi la cartella .zip
   - Rinominala in "ffmpeg"
   - Spostala nella directory "C:\"

2. **Apri le Impostazioni di Sistema**:
   - Premi `Windows + R` per aprire il prompt Esegui.
   - Digita `sysdm.cpl` e premi `Invio`.

3. **Accedi alle Variabili di Ambiente**:
   - Nella finestra di Proprietà di Sistema, fai clic su "Variabili d'ambiente".

4. **Modifica le Variabili di Sistema**:
   - Seleziona la variabile di sistema chiamata "Path" e fai clic su "Modifica...".

5. **Aggiungi `C:\ffmpeg\bin`**:
   - Fai clic su "Nuovo" e aggiungi `C:\ffmpeg\bin`.
   - Assicurati di separarlo dagli altri percorsi con un punto e virgola (`;`).

6. **Conferma e Chiudi**:
   - Clicca su "OK" per chiudere tutte le finestre di dialogo.

7. **Verifica**:
   - Apri un nuovo prompt dei comandi e digita `ffmpeg -version` per verificare l'aggiornamento.

### Configurazione di StudentCopilot

Scaricare la cartella dalla sezione "release" a destra. Una volta scaricata la cartella è sufficente decomprimerla e avviare il file "StudentCopilot.exe" per eseguire la prima configurazione. Alla fine di quest'ultima il programma sarà interamente utilizzabile e contenuto all'interno della medesima cartella, pronto per essere utilizzato; qualora non si voglia aprire continuamente la cartella originale è possibile spostarla in qualsiasi directory del proprio PC a avviare il programma attraverso un semplice collegamento al file "StudentCopilot.exe".
