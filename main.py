import youtube_dl
import speech_recognition as sr
import os
import lyricsgenius as lg

# from googletrans import Translator
# from __future__ import unicode_literals


################################################################################
################################################################################
### Download Youtube video as mp3

def download_song(song_url):
    """
    Download a song using youtube url and song title
    """
    ydl_opts = {
        'outtmpl': 'audios/%(title)s-%(id)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192'
        }],
        'postprocessor_args': [
            '-ar', '16000'
        ],
        'prefer_ffmpeg': True,
        'keepvideo': False
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([song_url])


youtube_links = ["https://www.youtube.com/watch?v=LKS-r_2XDBY",
                 "https://www.youtube.com/watch?v=qoee24_-bss",
                 "https://www.youtube.com/watch?v=1iYf-vINm8c"]

for link in youtube_links:
    download_song(link)


################################################################################
################################################################################
### Transform audio to text

FOLDER_AUDIO = "audios"
FOLDER_TEXT = "texts"
LANGUAGE = "en-US" # https://cloud.google.com/speech-to-text/docs/languages

print("starting...")

if not os.path.isdir(FOLDER_AUDIO):
    os.mkdir(FOLDER_AUDIO)

if not os.path.isdir(FOLDER_TEXT):
    os.mkdir(FOLDER_TEXT)

paths = [os.path.join(FOLDER_AUDIO, name) for name in os.listdir(FOLDER_AUDIO)]
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
### Grab lyrics from Genius API

def get_lyrics(artists, song_limit):
    c = 0
    for artist in artists:
        try:
            songs = (genius.search_artist(artist, max_songs=song_limit, sort='popularity')).songs
            song_lyrics_list = [song.lyrics for song in songs]
            file = open(f"{artist}_lyrics_of_{len(song_lyrics_list)}_songs.txt", "w", encoding='utf-8')
            file.write("\n \n \n \n \n".join(song_lyrics_list))
            c += 1
            print(f"Songs grabbed:{len(song_lyrics_list)}")
            file.close()
            print("___________________________________________________\n\n\n\n")
        except:
            print(f"some exception at {artist}: {c}")

api_key = "fRQM59H4driQWn2tVpNr7mlUM-7eVp8vwthjcd1pfG2BMcGNaZzq_C_bPw-Nk8pM"
genius = lg.Genius(api_key,
                   skip_non_songs=True,
                   excluded_terms=["Freestyle", "(Live)"],
                   remove_section_headers=True)

lyrics = get_lyrics(["Action Bronson"], 50)


##################################################################
##################################################################
### Lyrics pre-processing

remove_words = ['Lyrics', 'Embed'] #For some reason "embed" shows up at the end of each song with a # next to it

with open('texts/Action Bronson_lyrics_of_50_songs.txt') as oldfile, open('texts/Action Bronson_lyrics_of_50_songs_v2.txt', 'w') as newfile:
    for line in oldfile:
        if not any(word in line for word in remove_words):
            newfile.write(line)

## This may remove just the word from each line:
# bad_words = ['abc', 'def', 'ghi', 'jkl']
#
# with open('List of words.txt') as badfile, open('Clean list of words.txt', 'w') as cleanfile:
#     for line in badfile:
#         clean = True
#         for word in bad_words:
#             if word in line:
#                 clean = False
#         if clean == True:
#             cleanfile.write(line)