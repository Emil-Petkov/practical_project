import pyttsx3
import time


def speak_python(text):
    engine.say(text)
    engine.runAndWait()


engine = pyttsx3.init()

print("""* For exit() on the program write End command.
______________________________________________
""")

text = input(">>> ")

while text != "End" and text != "END" and text != "end":
    speak_python(text)
    text = input(">>> ")

print("\nHave a nice day my friend : )")
speak_python("Have a nice day my friend : )")
time.sleep(5)
