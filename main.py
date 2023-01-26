import speech_recognition as sr
import pyttsx3

audio = sr.recognizer()
maquina = pyttsx3.init()
maquina.say("Ola, eu sou a Cameline")
maquina.say("Como posso ajudar?")
maquina.runAndWait()

try:
    with sr.Microphone() as source:
        print("Ouvindo...")
        voz = audio.listen(source)
        comando = audio.recognizer_google(voz, language='pt-BR')
        comando = comando.lower()
        if 'cameline' in comando:
            print(comando)
except:
    print("Microfone está desligado")
