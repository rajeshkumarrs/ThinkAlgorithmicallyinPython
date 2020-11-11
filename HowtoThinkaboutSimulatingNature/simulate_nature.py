import tkinter
import time

# def countdown():
#     countlabel.configure(background="white")
#     howlong = int(textbox.get())
#     for i in range(howlong,0,-1):
#         countlabel.configure(text=i)
#         window.update()
#         time.sleep(1)
#     countlabel.configure(text="DONE!")

window = tkinter.Tk()
window.geometry("1000x1000")
window.title("My first GUI")
window.configure(background="grey")

# lbl = tkinter.Label(window, text="How many seconds to count down?")
# lbl.pack()
# textbox = tkinter.Entry(window)
# textbox.pack()
# count = tkinter.Button(window, text="Countdown!", command=countdown)
# count.pack()
# countlabel = tkinter.Label(window, height="10", width="10")
# countlabel.pack()

window.mainloop()

