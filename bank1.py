import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# ------------------ ОСНОВНОЕ ОКНО ------------------

root = tk.Tk()
root.title("Уралсиб Business")
root.geometry("1300x750")
root.configure(bg="#f2f2f7")
root.resizable(False, False)

saved_login = ""
saved_password = ""

# ------------------ СТИЛИ ------------------

style = ttk.Style()
style.theme_use("clam")

PRIMARY = "#5a2d91"
DARK = "#3c1361"
BG = "#f2f2f7"
WHITE = "#ffffff"

# ------------------ ЛЕВАЯ ПАНЕЛЬ ------------------

left = tk.Frame(root, bg=PRIMARY, width=300)
left.pack(side="left", fill="y")

tk.Label(left, text="Уралсиб",
         bg=PRIMARY, fg="white",
         font=("Segoe UI", 22, "bold")).pack(pady=40)

login_entry = tk.Entry(left, font=("Segoe UI", 12))
login_entry.pack(pady=10, ipadx=10, ipady=8)

password_entry = tk.Entry(left, show="*", font=("Segoe UI", 12))
password_entry.pack(pady=10, ipadx=10, ipady=8)

remember_var = tk.IntVar()
tk.Checkbutton(left, text="Запомнить логин",
               variable=remember_var,
               bg=PRIMARY, fg="white",
               selectcolor=PRIMARY,
               activebackground=PRIMARY).pack(pady=10)

# ------------------ ЦЕНТР ------------------

center = tk.Frame(root, bg=BG)
center.pack(side="left", expand=True, fill="both")

title = tk.Label(center,
                 text="УМНАЯ СИСТЕМА ПЕРЕВОДОВ\nС ВНЕДРЕНИЕМ СОВРЕМЕННЫХ ИИ",
                 bg=BG,
                 font=("Segoe UI", 18, "bold"))
title.pack(pady=30)

card_frame = tk.Frame(center, bg=PRIMARY, padx=30, pady=30)
card_frame.pack(pady=20)

tk.Label(card_frame, text="Уралсиб Business",
         bg=PRIMARY, fg="white",
         font=("Segoe UI", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

card_entry = tk.Entry(card_frame, font=("Segoe UI", 12))
card_entry.grid(row=1, column=0, columnspan=2, pady=10, ipadx=80, ipady=8)

date_entry = tk.Entry(card_frame, font=("Segoe UI", 12), width=10)
date_entry.grid(row=2, column=0, pady=10, ipadx=10, ipady=8)

cvc_entry = tk.Entry(card_frame, font=("Segoe UI", 12), width=10)
cvc_entry.grid(row=2, column=1, pady=10, ipadx=10, ipady=8)

tk.Label(card_frame, text="Сумма перевода",
         bg=PRIMARY, fg="white").grid(row=3, column=0, columnspan=2)

amount_entry = tk.Entry(card_frame, font=("Segoe UI", 12))
amount_entry.grid(row=4, column=0, columnspan=2, pady=10, ipadx=80, ipady=8)

tk.Label(card_frame, text="Сообщение получателю",
         bg=PRIMARY, fg="white").grid(row=5, column=0, columnspan=2)

message_entry = tk.Entry(card_frame, font=("Segoe UI", 12))
message_entry.grid(row=6, column=0, columnspan=2, pady=10, ipadx=80, ipady=8)

status_label = tk.Label(card_frame, text="", bg=PRIMARY, fg="white",
                        font=("Segoe UI", 10, "bold"))
status_label.grid(row=8, column=0, columnspan=2, pady=10)

# ------------------ ПРАВАЯ ПАНЕЛЬ ------------------

right = tk.Frame(root, bg="white", width=300)
right.pack(side="right", fill="y")

tk.Label(right, text="НАМ ДОВЕРЯЮТ",
         bg="white",
         font=("Segoe UI", 14, "bold")).pack(pady=20)

try:
    img = Image.open("trusted.png")
    img = img.resize((260, 550))
    photo = ImageTk.PhotoImage(img)
    tk.Label(right, image=photo, bg="white").pack()
except:
    tk.Label(right, text="(Картинка не найдена)",
             bg="white").pack()

# ------------------ ЛОГИКА ------------------

def luhn_check(card_number):
    card_number = card_number.replace(" ", "")
    if not card_number.isdigit():
        return False

    total = 0
    reverse_digits = card_number[::-1]

    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n

    return total % 10 == 0


def register():
    global saved_login, saved_password
    saved_login = login_entry.get()
    saved_password = password_entry.get()
    status_label.config(text="✔️ Аккаунт создан!", fg="lightgreen")
def login():
    if login_entry.get() == saved_login and password_entry.get() == saved_password:
        status_label.config(text="✔️ Авторизация успешна!", fg="lightgreen")
    else:
        status_label.config(text="✖️ Неверный логин или пароль", fg="red")


def transfer():
    card = card_entry.get()
    amount = amount_entry.get()

    if not luhn_check(card):
        status_label.config(text="✖️ Неверный номер карты", fg="red")
        return

    if amount == "" or not amount.isdigit():
        status_label.config(text="✖️ Введите корректную сумму", fg="red")
        return

    status_label.config(text="✔️ Перевод успешно выполнен!", fg="lightgreen")


# ------------------ КНОПКИ ------------------

def styled_button(parent, text, command):
    btn = tk.Button(parent, text=text,
                    bg=DARK, fg="white",
                    font=("Segoe UI", 11, "bold"),
                    activebackground="#2a0d47",
                    relief="flat",
                    command=command)
    return btn

styled_button(left, "АВТОРИЗОВАТЬСЯ", login).pack(pady=10, ipadx=10, ipady=8)
styled_button(left, "ЗАРЕГИСТРИРОВАТЬСЯ", register).pack(pady=10, ipadx=10, ipady=8)
styled_button(card_frame, "ПЕРЕВЕСТИ", transfer).grid(row=7, column=0, columnspan=2, pady=15, ipadx=40, ipady=8)

# ------------------ ЗАПУСК ------------------

root.mainloop()
