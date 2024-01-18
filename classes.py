from guizero import *


class LanguageSelector:
    def __init__(self):
        self.languages = {
            'english': 'en',
            'italian': 'it',
            'russian': 'ru',
            'german': 'de',
            'spanish': 'es',
            'french': 'fr',
            'polish': 'pl',
            'japanese': 'ja',
            'arabic': 'ar',
            'urdu': 'ur',
            'turkish': 'tr',
            'farsi': 'fa',
            'punjab': 'pa',
        }

    def print_language_choices(self):
        print("Available languages:\n")
        for language, code in self.languages.items():
            print(f"{language}")
    
    def get_user_input(self):
        self.print_language_choices()
        while True:
            user_input = input("\nEnter the language you would like to learn: ").lower()
            if user_input in self.languages:
                return user_input
            else:
                print("Language not detected. Please try another or check your spelling.")

    def select_language(self):
        language = self.get_user_input()
        select_language = self.languages[language]
        print(f"You selected {language} (Language code: {select_language}).")
        return select_language



class Process:
    def __init__(self, language_in, language_out):
        self.language_in = language_in
        self.language_out = language_out



class PhraseWriter:
    def __init__(self, filename="phrases.txt"):
        self.filename = filename

    def write_phrases(self, phrases):
        with open(self.filename, 'a') as file:
            for phrase in phrases:
                file.write(phrase + '\n')

    def read_phrases(self):
        with open(self.filename, 'r') as file:
            return file.readlines()
        
    def clear_phrases(self):
        with open(self.filename, 'w') as file:
            file.truncate(0)

