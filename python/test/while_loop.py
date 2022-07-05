while True:
    speak("How can I help you?")
    voice = recognize_speech().lower()
    print(voice)
    if 'open google' in voice:
        speak('Opening google..')
        s.execute_script("window.open('');")
        window_list = s.window_handles
        s.switch_to.window(window_list[-1])
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
    elif 'open online exam' in voice:
        speak('Opening exam..')
        s.execute_script("window.open('');")
        window_list = s.window_handles
        s.switch_to.window(window_list[-1])
        s.get('file:///D:/Quiz%20Application%20with%20Timer/index.html')
    elif 'start exam' in voice:
       element=s.find_element(By.XPATH,'//*[@id="1"]')
       element.click()  
       element=s.find_element(By.XPATH,'/html/body/div[2]/div/button[2]')
       element.click()
       
       trr=html.fromstring(s.page_source)
       
       
       #l =  extractQuestion(ree.content)

       l=trr.xpath('/html/body/div[3]/section/div[1]')
    #    print(l)
    #    print(l[0])
       engine.say(l)
       t=s.find_element(By.XPATH,'/html/body/div[3]/section/div[1]/span').text
       tn=t
       my=gTTS(text=tn,lang=language)
       my.save("welcome.mp3")
       os.system("mpg321 welcome.mp3")
       
              
    elif 'open exam' in voice:
        while True:
            speak('I am listening..')
            query = recognize_speech()
            if query != 'Error':
                break
        element=s.find_element_by_class_name('start_btn')
        element.click()
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
