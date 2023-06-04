import pyttsx3
import time


def speak_python(text):
    engine.say(text)
    engine.runAndWait()


engine = pyttsx3.init()

print("""* For exit() on the program write "End" command.
                                   ___

Write anything and your computer will read the message.
** Only English language is supported. **
""")

text = input("🤖: ")

while text != "End" and text != "END" and text != "end":
    speak_python(text)
    text = input("🤖: ")

print("""\n🤖: Have a nice day my friend : )
_________________________________""")
speak_python("Have a nice day my friend : )")

print("\nТhe program will close automatically after 5 seconds.")
time.sleep(5)

