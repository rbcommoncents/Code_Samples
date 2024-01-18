from gtts import gTTS
import translators as ts
import os
from playsound import playsound
import time
from classes import LanguageSelector
from guizero import *


practice_phrases = ["Where can I buy some food?", "He was bold.", "She was brave.", "Intelligence", "They had children that sang and played.",
                     "Why did the bicycle fall over?", "Because it was two-tired from all the compliments!", "What do you call a fake noodle?", "an impasta!", "Hello", 
                     "If you have not heard it already today.", "I Love you", "I am always thinking about you.", "and", 
                     "You look as beautiful as the day you came into this world.", "Today is..", "Is there anything I can do to help?", "Have a wonderful day, lined with blessings.",
                     "Why don't scientist trust atoms?", "Because they make up everything.", "How do you organize a space party?", "You planet!",
                     ]

def Play(txt):
    selector = LanguageSelector()
    lang = selector.select_language()
    
    app = App(title="Language Learning")
    options = Text(app, text=lang)

    app.display()

    for i in txt:
        print(i)
        myobj = gTTS(text=i, lang='en', slow=False)
        myobj.save('enSoundFile.mp3')
        playsound('enSoundFile.mp3')

        filename = f"{lang}SoundFile.mp3"
        text = ts.translate_text(i, to_language=lang)
        print(text)

        sound = gTTS(text=text, lang=lang, slow=True)
        sound.save(filename)

        playsound(filename)
        time.sleep(1)
        playsound(filename)

        time.sleep(2)


if __name__ == "__main__":
    Play(practice_phrases)