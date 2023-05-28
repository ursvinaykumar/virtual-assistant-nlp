import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser

listener = sr.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    global instruction

    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = listener.listen(source)
            instruction = listener.recognize_google(audio)
            instruction = instruction.lower()
            if "chimtu" in instruction:
                instruction = instruction.replace('chimtu', '')
            print(instruction)

    except sr.UnknownValueError:
        pass

    return instruction

def play_chimtu():
    instruction = input_instruction()
    print(instruction)

    if "play" in instruction:
        song = instruction.replace('play', '')
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + current_time)

    elif 'date' in instruction:
        current_date = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Today's date is " + current_date)

    elif 'how are you' in instruction:
        talk('I am fine, how about you?')

    elif 'what is your name' in instruction:
        talk('I am Chimtu, what can I do for you?')

    elif 'who is' in instruction:
        person = instruction.replace('who is', '').strip()
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'open' in instruction:
        website = instruction.replace('open', '').strip()
        talk('Opening ' + website)
        webbrowser.open('https://' + website)

    else:
        talk('Please repeat')

play_chimtu()
