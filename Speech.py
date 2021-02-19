from gtts import gTTS
import sys
import os


# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed

text = sys.argv[1]
speech_file = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
speech_file.save("speech_audio.mp3")

# Playing the converted file
os.system("mpg321 speech_audio.mp3")
