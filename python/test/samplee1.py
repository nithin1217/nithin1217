from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import speech_recognition as sr
import time
import pyttsx3
ser = Service("C:\\Users\\navinithin\\Downloads\\chromedriver.exe")
op = webdriver.ChromeOptions()
s = webdriver.Chrome(service=ser, options=op)

s.maximize_window()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speak(query):
    engine.say(query)
    engine.runAndWait()

def recognize_speech():
    with microphone as source:
        audio = recognizer.listen(source, phrase_time_limit=5)
    response = ""
    speak("Identifying speech..")
    try:
        response = recognizer.recognize_google(audio)
    except:
        response = "Error"
    return response
time.sleep(3)
speak("Hello master! I am now online..")
while True:
    speak("How can I help you?")
    voice = recognize_speech().lower()
    print(voice)
    if 'open google' in voice:
        speak('Opening google..')
        s.execute_script("window.open('');")
        window_list = s.window_handles
        s.switch_to_window(window_list[-1])
        s.get('https://google.com')
    elif 'search google' in voice:
        while True:
            speak('I am listening..')
            query = recognize_speech()
            if query != 'Error':
                break
        element = s.find_element_by_name('q')
        element.clear()
        element.send_keys(query)
        element.send_keys(Keys.RETURN)
    elif 'open youtube' in voice:
        speak('Opening youtube..')
        s.execute_script("window.open('');")
        window_list = s.window_handles
        s.switch_to_window(window_list[-1])
        s.get('https://youtube.com')
    elif 'search youtube' in voice:
        while True:
            speak('I am listening..')
            query = recognize_speech()
            if query != 'Error':
                break
        element = s.find_element_by_name('search_query')
        element.clear()
        element.send_keys(query)
        element.send_keys(Keys.RETURN)
    elif 'switch tab' in voice:
        num_tabs = len(s.window_handles)
        cur_tab = 0
        for i in range(num_tabs):
            if s.window_handles[i] == s.current_window_handle:
                if i != num_tabs - 1:
                    cur_tab = i + 1
                    break
        s.switch_to_window(s.window_handles[cur_tab])
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
    time.sleep(2)