from tkinter import *

import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
Y_ORANGE="#ffd59e"
BLUE="#4700d8"
NEON_GREEN="#06ff00"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer= None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_all():
    window.after_cancel(timer)

    # timer_text 00:00
    canvas.itemconfig(timer_text, text=f"00:00")

    #section= "Timer"
    section["text"]= "Timer"
    section["fg"]= BLUE

    #reset_checkmarks
    checkmarks["text"]=""
    global reps
    reps= 0




# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_secs)
        section["text"]="Break"
        section["fg"]= RED

        # If it is the 2, 4, 6 rep
    elif reps % 2 == 0:
        countdown(short_break_secs)
        section["text"]= "Break"
        section["fg"]= PINK


    else:
        countdown(work_secs)
        section["text"]= "Work"
        section["fg"]= NEON_GREEN



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60




    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark=""
        work_sessions= math.floor(reps/2)
        for each_mark in range (work_sessions):
            mark+= "✔"
        checkmarks["text"]= mark















# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=Y_ORANGE)

canvas= Canvas(width= 200, height= 224 ,bg=Y_ORANGE, highlightthickness=0)
tomato_image= PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_image)
timer_text=canvas.create_text(100,132, text= "00:00",fill="white", font=(FONT_NAME, 37, "bold"))

canvas.grid(row=1, column=1)


#section , work or rest
section= Label(text="Timer", font=("Comic", 30, 'italic'), fg=BLUE, bg=Y_ORANGE)
section.grid(row=0, column=1)

#start button

start= Button(text="Start", bg="white", fg=NEON_GREEN, highlightthickness=0, command=start_timer)

start.config(padx=5, pady=5)
start.grid(row=2, column=0)

#reset button

reset= Button(text="Reset", bg="white", fg=RED,  highlightthickness=0, command=reset_all)
reset.config(padx=5, pady=5)
reset.grid(row=2, column=2)

#Checkmarks how many Pomodoro

checkmarks= Label(font=(FONT_NAME, 15, "normal"), fg=NEON_GREEN, bg=Y_ORANGE)
checkmarks.grid(row=3, column=1)







window.mainloop()

