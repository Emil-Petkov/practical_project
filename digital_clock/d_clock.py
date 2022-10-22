import tkinter as tk
import time

window = tk.Tk()


def update_clock():
    hours = time.strftime("%H")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    time_text = f"{hours}:{minutes}:{seconds} {am_or_pm}"
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000, update_clock) #1000 ms == 1 second


digital_clock_lbl = tk.Label(window, text="00:00:00", font="Helvetica 100 bold")
digital_clock_lbl.pack()

update_clock()

window.mainloop()
