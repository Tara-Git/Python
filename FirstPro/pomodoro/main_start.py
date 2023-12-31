from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
# colors from https://colorhunt.co/
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
mark = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_button():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="0:0")
    label.config(text="Let's Rock! :D")
    global mark
    mark = ""
    check_marks.config(text=mark)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_button():
    # print("start")
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it is the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Long Break Enjoy! <3", fg=RED, bg=YELLOW)
    # If it is the 1st/3rd/5th/7th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Short Brk, Keep Going! ;)", fg=PINK, bg=YELLOW)
    # If it is the 2nd/4th/6th rep:
    else:
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_button()
        global mark
        global reps
        if reps % 2 == 0:
            mark += "🗸"
            check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="Let's Rock! :D", font=(FONT_NAME, 35, "bold"), fg="green", highlightthickness=0, bg=YELLOW)
label.grid(column=1, row=0)

check_marks = Label(font=(FONT_NAME, 25, "bold"), fg="green", bg=YELLOW)
check_marks.grid(column=1, row=3)


button01 = Button(text="Start", command=start_button, highlightthickness=0)
button01.grid(column=0, row=2)

button02 = Button(text="Reset", command=reset_button, highlightthickness=0)
button02.grid(column=2, row=2)

window.mainloop()
window.mainloop()
