import speech_recognition as sr

recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.05)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print("Recognized Voice: ", text)
    except:
        recognizer = sr.Recognizer()
        continue

