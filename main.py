import speech_recognition as sr
import os

from googletrans import Translator

FOLDER_AUDIO = "audios"
FOLDER_TEXT = "texts"
LANGUAGE = "en-US" # https://cloud.google.com/speech-to-text/docs/languages

print("starting...")

if not os.path.isdir(FOLDER_AUDIO):
    os.mkdir(FOLDER_AUDIO)
    
if not os.path.isdir(FOLDER_TEXT):
    os.mkdir(FOLDER_TEXT)

paths = [os.path.join(FOLDER_AUDIO, nome) for nome in os.listdir(FOLDER_AUDIO)]
files = [arq for arq in paths if os.path.isfile(arq)]
wav_files = [arq for arq in files if arq.lower().endswith(".wav")]

for filename in wav_files:
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = r.record(source)

    command = r.recognize_google(audio, language=LANGUAGE)

    print("running file {}".format(filename))

    filefinal = filename.split("audios/")[1].split(".wav")[0]
    filefinal = '{}/{}.txt'.format(FOLDER_TEXT, filefinal)
    with open(filefinal, 'w') as arq:
        arq.write(str(command))

    print("create a new file {}".format(filefinal))

print("finish")



##################################################################
##################################################################
### Read text and translate from Dutch to English

# translator = Translator()
#
# # open text file in read mode
# text_file = open("D:/data.txt", "r")
#
# # read whole file to a string
# data = text_file.read()
#
# # close file
# text_file.close()
#
# print(data)