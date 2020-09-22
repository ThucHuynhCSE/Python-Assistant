import pyttsx3
import speech_recognition
from datetime import date, datetime

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()
robot_brain = ""

while (True):
    # hear
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You" + you)

    # brain
    print("Robot: ... ")
    if you == "":
        robot_brain = "I cant hear you, try again"
    elif "hello" in you:
        robot_brain = "Hello Thuk"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "bye" in you:
        robot_brain = "Goodbye, Thank"
        robot_mouth.say("Robot: " + robot_brain)
        robot_mouth.runAndWait()
        break
    # say
    robot_mouth.say("Robot: " + robot_brain)
    robot_mouth.runAndWait()
