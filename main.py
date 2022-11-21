import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import subprocess


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening')

        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("Recognizing")

            Query = r.recognize_google(audio, language='fr-FR')
            print("the command is printed=", Query)

        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return Query


def speak(audio):

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0].id)

    engine.say(audio)

    engine.runAndWait()


def tellDay():

    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Lundi', 2: 'Mardi',
                3: 'Mercredi', 4: 'Jeudi',
                5: 'Vendredi', 6: 'Samedi',
                7: 'Dimanche'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("AUjourd'hui, nous sommes " + day_of_the_week)


def tellTime():

    time = str(datetime.datetime.now())

    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("Il est" + hour + "heures " + min)


def Hello():

    speak("Bonjor maître, je suis votre assistante personnel, que pis-je faire pour vous ?")


def Take_query():

    Hello()

    while(True):
        named="alice"
        query = takeCommand().lower()
        if query.startswith("Alice "):
            if "ouvre internet" in query:
                speak("Google se lance")
                webbrowser.open("www.google.com")
                continue

            elif "il est quel jour" in query:
                tellDay()
                continue

            elif "il est quelle heure" in query:
                tellTime()
                continue

            elif "au revoir" in query:
                speak("Au revoir maitre !")
                exit()

            elif "assistant comment t'appelles-tu" in query:
                speak("je m'appelle" + named)

            elif "sur youtube recherche " in query:
                query = query.replace("sur youtube recherche ", "")
                speak("Voici votre recherche")
                webbrowser.open("https://www.youtube.com/results?search_query=" + query)

            elif "sur google recherche " in query:
                query = query.replace("sur google recherche ", "")
                speak("Voici votre recherche")
                webbrowser.open("https://www.google.com/search?q=" + query)

        


if __name__ == '__main__':

    Take_query()
