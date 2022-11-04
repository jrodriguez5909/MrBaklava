<p align="center">
  <img src="./img/action-bronson-gq-1.webp" alt="Statoscope example" width="650">
</p>

# Bronsoliño, _wtf are you saying?!_
In this project I attempt to decipher Action Bronson's rap formula and the themes he raps about the most in his tracks. My project references several other projects:
* **[youtube_dl](https://pypi.org/project/youtube_dl/)** to download several acapellas
* **[speech_recogntion](https://pypi.org/project/SpeechRecognition/)** to convert audio to text files
* **[lyricsgenius](https://lyricsgenius.readthedocs.io/en/master/)** to grab high-quality lyrics
* tbd


## Sourcing lyrics
I started trying to source lyrics from audio files downloaded through YouTube using **[youtube_dl](https://pypi.org/project/youtube_dl/)** then using **[speech_recogntion](https://pypi.org/project/SpeechRecognition/)** to grab text from the audio and this worked OK with the XXL Freshman freestyle since there were no pauses and no traces from the filtered instrumental for acapellas. The speech recognition API struggled with acapellas stripped from songs where there were pauses or traces of the instrumental (see these files in the "texts" folder).

I resorted to **[lyricsgenius](https://lyricsgenius.readthedocs.io/en/master/)** for grabbing lyrics so I could focus on the nlp part of the project.


## NLP methodology
See the **[NLP_analysis.ipynb](https://github.com/jrodriguez5909/MrBaklava/blob/master/NLP_analysis.ipynb)** notebook for the full analysis on lyrics. Here's a little spoiler in case you're not interested in delving into jupyter notebooks.

### Word frequency:
<p align="center">
  <img src="./img/word_frequency.png" alt="Statoscope example" width="400">
</p>

### Word cloud:
<p align="center">
  <img src="./img/word_cloud.png" alt="Statoscope example" width="400">
</p>