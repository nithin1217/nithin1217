from logging import exception
from shutil import move
from warnings import catch_warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import speech_recognition as sr
import time
import pyttsx3
from gtts import gTTS
import os
from lxml import html
import requests
from bs4 import BeautifulSoup
import re


def speak(query):
    engine.say(query)
    engine.runAndWait()

def recognize_speech():
    with microphone as source:
        recognizer.energy_threshold=1000
        audio = recognizer.listen(source, phrase_time_limit=5)
    response = ""
    speak("Identifying speech..")
    try:
        response = recognizer.recognize_google(audio)
    except:
        response = "Error"
    return response

def extractQuestion(con):
    reg_str = '<p>(.*)</p>'
    res = re.findall(reg_str, con)
    return str(res[0])

def extractOptions(con):
    reg_str = '(?<=<span>)([\w|\d|\n|\s]*)(?=<\/span>)'
    res = re.findall(reg_str, con)
    return res  

def extractSection(con):
    reg_str = '<section>(\s.*\s.*\s.*)</section>'
    return re.findall(reg_str, con)

  


def speakQuestion():
    src = driver.page_source
    section = extractSection(src)[0]
    options = extractOptions(section)
    ques =  extractQuestion(section)
    speak('Question number')
    speak(ques)
    speak('Options are')

    for i in options:
        speak(str(i))


def onStart():
    element=driver.find_element(By.XPATH,'//*[@id="1"]')
    element.click() 
    element=driver.find_element(By.XPATH,'/html/body/div[2]/div/button[2]')
    element.click()




driver = webdriver.Chrome("D:\Quiz Application with Timer\python\driver\chromedriver.exe")
url= "https://nithin1217.github.io"
driver.get(url)
driver.maximize_window()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
language ='en'
recognizer = sr.Recognizer()
microphone = sr.Microphone()

time.sleep(1)
speak("You  are  Entered  Exam  Portal!")
while True:
    time.sleep(2)
    speak("Give your valued Command..") 
    voice = recognize_speech().lower()
    if 'start' in voice:
        onStart()
        while 1:
            speakQuestion()
            break

        if 'option a' in voice:
            element=driver.find_element(By.XPATH,'/html/body/div[3]/section/div[2]/div[1]')
            element.click()
            speak('wrong Answer')
            element=driver.find_element(By.XPATH,'/html/body/div[3]/footer/button')
            element.click()
            continue
    
        elif 'option b' in voice:
            element=driver.find_element(By.XPATH,'/html/body/div[3]/section/div[2]/div[2]')
            element.click()
            speak('Correct Answer') 
            element=driver.find_element(By.XPATH,'/html/body/div[3]/footer/button')
            element.click()

        elif 'option c' in voice:
            element=driver.find_element(By.XPATH,'/html/body/div[3]/section/div[2]/div[3]')
            element.click()
            speak('wrong Answer')
            element=driver.find_element(By.XPATH,'/html/body/div[3]/footer/button')
            element.click()

        elif 'option d' in voice:
            element=driver.find_element(By.XPATH,'/html/body/div[3]/section/div[2]/div[4]')
            element.click()
            speak('wrong Answer')
            element=driver.find_element(By.XPATH,'/html/body/div[3]/footer/button')
            element.click()

    elif 'close tab' in voice:
        speak('Closing Tab..')
        element.close()
    elif 'go back' in voice:
        element.back()
    elif 'go forward' in voice:
        element.forward()
    elif 'exit' in voice:
        speak('Goodbye Master!')
        element.quit()
        break
    

# while 1:
    # speak("How can I help you?")
    # voice = recognize_speech().lower()
    # if('start' in voice):
    #     onStart()
    #     while True:
    #         cmove()

 # url="file:///D:/Quiz%20Application%20with%20Timer/index.html"# ser = Service("C:\\Users\\navinithin\\Downloads\\chromedriver.exe")
# op = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=ser, options=op)