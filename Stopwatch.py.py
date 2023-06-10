import tkinter as tk
root=tk.Tk()
root.title("Stopwatch")
root.geometry('300x300')
label=tk.Label(root,text="00:00:00")
label.pack()
running=True
def sta():
       global running
       m = label.cget('text').split(":")
       hour = m[0]
       minute = m[1]
       seconds = m[2]

       if(running):
            if int(seconds) == 59:
                seconds = '00'
                if int(minute) == 59:
                    minute = '00'
                    if int(hour) < 12:
                        hour = str(int(hour) + 1).zfill(2)
                    else:
                        hour = '00'
                else:
                    minute = str(int(minute) + 1).zfill(2)
            else:
                seconds = str(int(seconds) + 1).zfill(2)

            current_time = f'{hour}:{minute}:{seconds}'
            label.config(text=current_time)

            root.after(1000, sta)





Submit=tk.Button(root,text="Start",command=sta)
Submit.pack()
def sto():
    global running
    running=False

Submit=tk.Button(root,text="Stop",command=sto)
Submit.pack()
def res():
    global running
    running=False
    label.config(text="00:00:00")



Submit=tk.Button(root,text="Reset",command=res)
Submit.pack()
root.mainloop()







#