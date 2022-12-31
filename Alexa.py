import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# engine.say('I am your assistant .')
# engine.say("What can I do for you ?")
def talk(text):
    engine.say(text)
    # engine.say("What can I do for you ?")
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'search' in command:
        search = command.replace('search', '')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        talk('Here I found ' + search)
    elif 'where is ' in command:
        location = command.replace('where is ', '')
        url = 'https://google.nl/maps/place/' + location
        webbrowser.get().open(url)
        talk('Location of' + location + 'is')
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
