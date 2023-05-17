import pyttsx3
from gtts import *
import random
import time
from tempfile import TemporaryFile
import playsound
def offline():
    verb=[]
    answer=[]
    def say(str):
        engine = pyttsx3.init()
        engine.say(str)
        engine.runAndWait()
    def main(list):
        global answer
        answer=list.copy()
        tts=pyttsx3.init()
        random.shuffle(answer)
        say("First, I will read them fast.")
        
        say("after that, I will read them slower.")
        
        say("I will repeat these verbs three times. At the end, I will repeat every verbs again, so that you can check your answers.")
        
        say("You now have five seconds to prepare for the self-dictation.")
        
        time.sleep(5)
        say("Self-dictation will start now.")
        time.sleep(1)
        say("Now, I will read them fast.")
        
        time.sleep(0.5)
        for i in range(0,len(answer)):
            say(answer[i])
            
            time.sleep(0.5)
        say("Now, I will read them slower\n")
        
        time.sleep(0.5)
        for i in range(0,len(list)):
            for x in range(3):
                say(f"{i+1}.")
                
                say(f"{answer[i]}")
                time.sleep(1.5)
        say("Now, I will repeat them again.")
        
        time.sleep(0.5)
        for i in range(0,len(list)):
            say(f"{i+1}.")
            say(answer[i])
            
            time.sleep(0.5)
        say("If you need the answer, type getanswer.")
        
    def init():
        tts=pyttsx3.init()
        print("Welcome to use English Self-Dictation Assistant.")
        say("Welcome to use English Self-Dictation Assistant.")
        
        print("I can help you to do a self-dictation without other people.")
        say("I can help you to do a self-dictation without other people.")
        
        print("You can type add $whatever to add vocab to the list, after that, type start to start the self-dictation.")
        say("You can type add $whatever to add vocab to the list, after that, type start to start the self-dictation.")
        
        print("If you want to clear the list, type clear.")
        say("If you want to clear the list, type clear.")
        
        print("You can type view to see all the verbs in the list, then you can use delete $thenumberoftheverb to remove any verbs.")
        say("You can type view to see all the verbs in the list, then you can use delete $thenumberoftheverb to remove any verbs.")
        
    def checkcommand(command):
        global verb
        global answer
        if command=="clear":
            verb=[]
        elif command[0:4]=="add ":
            verb.append(command[4:])
        elif command=="view":
            print(verb)
        elif command[0:7]=="delete":
            x=int(command[7:])
            verb[x].remove()
        elif command=="start":
            main(verb)
        elif command=="getanswer":
            print(answer)
        elif command=="exit":
            return 0
        else:
            pass
    init()
    while True:
        print("")
        command=input("command > ")
        checkcommand(command)
def online():
    verb=[]
    answer=[]
    def say(str):
        tts = gTTS(text=str, lang='en')
        f = TemporaryFile()
        tts.save('temp.mp3')
        playsound.playsound('temp.mp3')
        f.close()
    def main(list):
        global answer
        answer=list.copy()
        random.shuffle(answer)
        say("First, I will read them fast.")
        
        say("after that, I will read them slower.")
        
        say("I will repeat these verbs three times. At the end, I will repeat every verbs again, so that you can check your answers.")
        
        say("You now have five seconds to prepare for the self-dictation.")
        
        time.sleep(5)
        say("Self-dictation will start now.")
        time.sleep(1)
        say("Now, I will read them fast.")
        
        time.sleep(0.5)
        for i in range(0,len(answer)):
            say(answer[i])
            
            time.sleep(0.5)
        say("Now, I will read them slower\n")
        
        time.sleep(0.5)
        for i in range(0,len(list)):
            for x in range(3):
                say(f"{i+1}.")
                
                say(f"{answer[i]}")
                time.sleep(1.5)
        say("Now, I will repeat them again.")
        
        time.sleep(0.5)
        for i in range(0,len(list)):
            say(f"{i+1}.")
            say(answer[i])
            
            time.sleep(0.5)
        say("If you need the answer, type getanswer.")
        
    def init():
        print("Welcome to use English Self-Dictation Assistant.")
        say("Welcome to use English Self-Dictation Assistant.")
        
        print("I can help you to do a self-dictation without other people.")
        say("I can help you to do a self-dictation without other people.")
        
        print("You can type add $whatever to add vocab to the list, after that, type start to start the self-dictation.")
        say("You can type add $whatever to add vocab to the list, after that, type start to start the self-dictation.")
        
        print("If you want to clear the list, type clear.")
        say("If you want to clear the list, type clear.")
        
        print("You can type view to see all the verbs in the list, then you can use delete $thenumberoftheverb to remove any verbs.")
        say("You can type view to see all the verbs in the list, then you can use delete $thenumberoftheverb to remove any verbs.")
        
    def checkcommand(command):
        global verb
        global answer
        if command=="clear":
            verb=[]
        elif command[0:4]=="add ":
            verb.append(command[4:])
        elif command=="view":
            print(verb)
        elif command[0:7]=="delete":
            x=int(command[7:])
            verb[x].remove()
        elif command=="start":
            main(verb)
        elif command=="getanswer":
            print(answer)
        elif command=="exit":
            return 0
        else:
            pass
    init()
    while True:
        print("")
        command=input("command > ")
        checkcommand(command)

while True:
    print("")
    choose=input("Online or Offline? (online/offline) > ")
    if choose == "online":
        online()
    elif choose == "offline":
        offline()
    elif choose == "exit":
        break