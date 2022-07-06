# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# import speech_recognition as sr
# import time
# import pyttsx3
# ser = Service("C:\\Users\\navinithin\\Downloads\\chromedriver.exe")
# op = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=ser, options=op)
# url= "https://nithin1217.github.io"
# driver.get(url)
# driver.maximize_window()

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

# recognizer = sr.Recognizer()
# microphone = sr.Microphone()

# def speak(query):
#     engine.say(query)
#     engine.runAndWait()

# def recognize_speech():
#     with microphone as source:
#         audio = recognizer.listen(source, phrase_time_limit=5)
#     response = ""
#     speak("Identifying speech..")
#     try:
#         response = recognizer.recognize_google(audio)
#     except:
#         response = "Error"
#     return response
# time.sleep(3)
# speak("Hi! I am now online")
# while True:
#     speak("How can I help you?")
#     voice = recognize_speech().lower()
#     print(voice)
#     if 'Start' in voice:
#          onStart()
#         while True:
#             cmove()
       
    elif 'close tab' in voice:
        speak('Closing Tab..')
        s.close()
    elif 'go back' in voice:
        s.back()
    elif 'go forward' in voice:
        s.forward()
    elif 'exit' in voice:
        speak('Goodbye Master!')
        s.quit()
        break
    else:
        speak('Not a valid command. Please try again.')
    time.sleep(1)