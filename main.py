import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime

# Initialisation du moteur de synthèse vocale
engine = ttx.init()
engine.setProperty('voice', 'french')

# Fonction pour parler
def parler(text):
    engine.say(text)
    engine.runAndWait()

# Fonction pour écouter avec gestion des erreurs
def ecouter():
    try:
        with sr.Microphone() as source:
            parler("Parlez maintenant")
            voix = listener.listen(source)
            command = listener.recognize_google(voix, language='fr-FR')
            command = command.lower()
    except sr.UnknownValueError:
        parler("Je n'ai pas compris. Pouvez-vous répéter ?")
        return ""
    except sr.RequestError:
        parler("Je ne parviens pas à accéder au service de reconnaissance vocale. Veuillez réessayer plus tard.")
        return ""
    return command

# Fonction pour jouer une chanson sur YouTube
def jouer_playlist(chanson):
    pywhatkit.playonyt(chanson)

# Fonction principale pour exécuter l'assistant
def run_assistant():
    command = ecouter()
    print(command)
    if 'mets la chanson de' in command or 'joue' in command:
        chanson = command.replace('mets la chanson de', '').replace('joue', '')
        parler(f"Je lance la playlist de {chanson}")
        jouer_playlist(chanson)
    elif 'heure' in command:
        heure = datetime.datetime.now().strftime("%H:%M")
        parler(f"Il est {heure}")
    elif 'bonjour' in command:
        parler("Bonjour, comment allez-vous ?")
    elif 'recherche sur Google' in command:
        requete = command.replace('recherche sur Google', '')
        parler(f"Voici les résultats de la recherche sur Google pour {requete}")
        pywhatkit.search(requete)
    elif 'définition de' in command:
        mot = command.replace('définition de', '')
        parler(f"Voici la définition de {mot}")
        pywhatkit.info(mot)
    else:
        parler("Désolé, je ne comprends pas.")

# Initialisation du recognizer
listener = sr.Recognizer()

# Boucle principale
while True:
    run_assistant()
