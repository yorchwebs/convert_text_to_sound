from gtts import gTTS
from data import load_data


import os

words = load_data()

language = "en"

current_directory = os.getcwd()

output_directory = os.path.join(current_directory, "translates")
os.makedirs(output_directory, exist_ok=True)

for word in words:
    myobj = gTTS(text=word, lang=language, slow=False)

    output_file = os.path.join(output_directory, f"{word}.mp3")
    myobj.save(output_file)
