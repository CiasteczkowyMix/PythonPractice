import speech_recognition as sr
import random
import time
choose = random.randint(0,1000)
i = 0
print('Hello in game!\nYour task is to guess the number between 0 and 1000\nGOOD LUCK')
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try: 
            text = r.recognize_google(audio)
        except:
            text = "error"
        a = format(text)
        print("You said: " + a)
        i = i+1
        if i == 7:
            print('If you want to leave, just say "bye"')
        if a.isdigit():
            if int(a) != choose:
                if int(a) < choose:
                    print("Correct number is higher")
                else:
                    print("Correct number is lower")
                time.sleep(3)
                print("Try again")
            elif int(a) == choose:
                print("You won after " + str(i) + " tries")
                exit()
        elif a == "bye":
            break
        else:
            print("Sorry, hard to check this, repeat please:")
            time.sleep(4.5)
print("Good Bye")