from tkinter import *

FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=(FONT_NAME, 10, "bold"))
website_label.grid(column=0, row=1)

website_text = Text(height=1, width=35)
website_text.focus()
website_text.insert(END, "")
website_text.grid(column=1, row=1, columnspan=2)

email_user_label = Label(text="Email/UserName:", font=(FONT_NAME, 10, "bold"))
email_user_label.grid(column=0, row=2)

email_user_text = Text(height=1, width=35)
email_user_text.focus()
email_user_text.insert(END, "")
email_user_text.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", font=(FONT_NAME, 10, "bold"))
password_label.grid(column=0, row=3)

password_text = Text(height=1, width=25)
password_text.focus()
password_text.insert(END, "")
password_text.grid(column=1, row=3)

password_button = Button(text="Generate Pass")
password_button.grid(column=2, row=3)

add_button = Button(text="Add", height=1, width=40)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()