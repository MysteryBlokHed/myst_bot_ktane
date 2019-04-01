# Created by MysteryBlokHed.
import speech_recognition as sr
import pyttsx3
import modules.wires, modules.button

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Calibrating...")
    r.adjust_for_ambient_noise(source)
    print("Done.")

tts = pyttsx3.init()

odd_serial = False
batteries = 0
serial_vowel = False
car_indicator = False
frk_indicator = False
parallel_port = False

def sanitize_colours(text):
    text = text.replace("read", "red")
    text = " ".join([colour for colour in text.split() if colour in ("red", "blue", "yellow", "black", "white")])
    return text

while True:
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        # Reset bomb variables
        if text[:10] == "bomb reset":
            odd_serial = False
            batteries = 0
            serial_vowel = False
            car_indicator = False
            frk_indicator = False
            parallel_port = False
        # Change last digit of serial number
        elif text[:13] == "serial number" or text[:13] == "cereal number":
            if int(text[-1]) in (1, 3, 5, 7, 9):
                odd_serial = True
                print(text)
                tts.say(text)
                tts.runAndWait()
            elif int(text[-1]) in (0, 2, 4, 6, 8):
                odd_serial = False
                print(text)
                tts.say(text)
                tts.runAndWait()
            else:
                print("Unrecognized command.")
        # Change amount of batteries
        elif text[:9] == "batteries":
            if text[-1] == "V":
                batteries = 5
                print(text)
                tts.say(text)
                tts.runAndWait()
            elif text.split()[1] == "to" or text.split()[1] == "too":
                batteries = 2
                print(text)
                tts.say(text)
                tts.runAndWait()
            elif text.split()[1] == "one":
                batteries = 1
                print(text)
                tts.say(text)
                tts.runAndWait()
            else:
                batteries = int(text[-1])
        # Change whether or not there is a vowel in the serial number
        elif text[:12] == "serial vowel" or text[:12] == "cereal vowel":
            if text.split()[2] == "yes":
                serial_vowel = True
                print(text)
                tts.say(text)
                tts.runAndWait()
            elif text.split()[2] == "no" or text.split()[2] == "know":
                serial_vowel = False
                print(text)
                tts.say(text)
                tts.runAndWait()
            else:
                print("Unrecognized command.")
        # Change whether or not there is a lit CAR indicator on the bomb
        elif text[:13] == "car indicator":
            if text.split()[2] == "yes":
                car_indicator = True
                print(text)
                tts.say(text)
                tts.runAndWait()
            elif text.split()[2] == "no" or text.split()[2] == "know":
                car_indicator = False
                print(text)
                tts.say(text)
                tts.runAndWait()
            else:
                print("Unrecognized command.")
        # Change whether or not there is a lit FRK indicator on the bomb
        elif text[:15] == "freak indicator":
            if text.split()[2] == "yes":
                frk_indicator = True
                print(text)
                tts.say(text)
                tts.runAndWait()
            elif text.split()[2] == "no" or text.split()[2] == "know":
                frk_indicator = False
                print(text)
                tts.say(text)
                tts.runAndWait()
            else:
                print("Unrecognized command.")
        # Change whether or not there is a parallel port on the bomb
        elif text[:13] == "parallel port":
            if text.split()[2] == "yes":
                parallel_port = True
                print(text)
                tts.say(text)
                tts.runAndWait()
            elif text.split()[2] == "no" or text.split()[2] == "know":
                parallel_port = False
                print(text)
                tts.say(text)
                tts.runAndWait()
            else:
                print("Unrecognized command.")
        # Defuse wires module
        elif text[:5] == "wires":
            print(text)
            tts.say(text)
            print(modules.wires.wires(sanitize_colours(text).split(), odd_serial))
            tts.say(modules.wires.wires(sanitize_colours(text).split(), odd_serial))
            tts.runAndWait()
        # Button colour strip instructions
        elif text[:12] == "button color":
            print(text)
            tts.say(text)
            print(modules.button.button_strip(sanitize_colours(text)))
            tts.say(modules.button.button_strip(sanitize_colours(text)))
            tts.runAndWait()
        # Defuse button module
        elif text[:6] == "button":
            print(text)
            tts.say(text)
            print(modules.button.button(sanitize_colours(text), text.split()[2], batteries, car_indicator, frk_indicator))
            tts.say(modules.button.button(sanitize_colours(text), text.split()[2], batteries, car_indicator, frk_indicator))
            tts.runAndWait()
        else:
            print("Unrecognized command.")
    except:
        print("Unrecognized command.")