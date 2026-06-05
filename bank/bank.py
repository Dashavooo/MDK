import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# ----------------- ОСНОВНОЕ ОКНО -----------------
root = tk.Tk()
root.title("Уралсиб")
root.geometry("1200x700")
root.configure(bg="#f2f2f7")

saved_login = ""
saved_password = ""

# ----------------- ЛЕВАЯ ПАНЕЛЬ -----------------
left_frame = tk.Frame(root, bg="#5a2d91", width=300)
left_frame.pack(side="left", fill="y")

tk.Label(left_frame, text="Уралсиб", bg="#5a2d91",
         fg="white", font=("Arial", 20, "bold")).pack(pady=30)

login_entry = tk.Entry(left_frame)
login_entry.pack(pady=10)

password_entry = tk.Entry(left_frame, show="*")
password_entry.pack(pady=10)

remember_var = tk.IntVar()
tk.Checkbutton(left_frame, text="Запомнить логин",
               bg="#5a2d91", fg="white",
               variable=remember_var).pack(pady=10)

# ----------------- ЦЕНТР -----------------
center_frame = tk.Frame(root, bg="#f2f2f7")
center_frame.pack(side="left", expand=True, fill="both")

title_label = tk.Label(center_frame,
                       text="УМНАЯ СИСТЕМА ПЕРЕВОДОВ\nС ВНЕДРЕНИЕМ СОВРЕМЕННЫХ ИИ!",
                       bg="#f2f2f7",
                       font=("Arial", 16, "bold"))
title_label.pack(pady=20)

card_frame = tk.Frame(center_frame, bg="#5a2d91", padx=20, pady=20)
card_frame.pack(pady=20)

tk.Label(card_frame, text="Уралсиб Business",
         bg="#5a2d91", fg="white",
         font=("Arial", 14, "bold")).pack(pady=10)

card_entry = tk.Entry(card_frame, width=30)
card_entry.pack(pady=5)

date_entry = tk.Entry(card_frame, width=10)
date_entry.pack(pady=5)

cvc_entry = tk.Entry(card_frame, width=10)
cvc_entry.pack(pady=5)

tk.Label(card_frame, text="Сумма перевода",
         bg="#5a2d91", fg="white").pack(pady=5)

amount_entry = tk.Entry(card_frame)
amount_entry.pack(pady=5)

tk.Label(card_frame, text="Сообщение получателю",
         bg="#5a2d91", fg="white").pack(pady=5)

message_entry = tk.Entry(card_frame)
message_entry.pack(pady=5)

# ----------------- ПРАВАЯ ПАНЕЛЬ -----------------
right_frame = tk.Frame(root, bg="white", width=300)
right_frame.pack(side="right", fill="y")

tk.Label(right_frame, text="НАМ ДОВЕРЯЮТ",
         bg="white", font=("Arial", 14, "bold")).pack(pady=20)

try:
    img = Image.open("../trusted.png")
    img = img.resize((250, 500))
    photo = ImageTk.PhotoImage(img)
    tk.Label(right_frame, image=photo, bg="white").pack()
except:
    tk.Label(right_frame, text="(Картинка не найдена)",
             bg="white").pack()

# ----------------- ФУНКЦИИ -----------------

def register():
    global saved_login, saved_password
    new_login = login_entry.get()
    new_password = password_entry.get()

    if new_login == "" or new_password == "":
        messagebox.showerror("Ошибка", "Заполните все поля")
        return

    saved_login = new_login
    saved_password = new_password
    messagebox.showinfo("Успех", "Аккаунт создан!")


def login():
    if login_entry.get() == saved_login and password_entry.get() == saved_password:
        messagebox.showinfo("Успех", "Авторизация успешна!")
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль")


def transfer():
    if card_entry.get() == "" or amount_entry.get() == "":
        messagebox.showerror("Ошибка", "Введите карту и сумму")
        return

    messagebox.showinfo("Успех", "Перевод выполнен!")


# ----------------- КНОПКИ -----------------
tk.Button(left_frame, text="АВТОРИЗОВАТЬСЯ",
          command=login, bg="#3c1361",
          fg="white").pack(pady=10)

tk.Button(left_frame, text="ЗАРЕГИСТРИРОВАТЬСЯ",
          command=register, bg="#3c1361",
          fg="white").pack(pady=10)

tk.Button(card_frame, text="ПЕРЕВЕСТИ",
          command=transfer, bg="#3c1361",
          fg="white").pack(pady=15)

# ----------------- ЗАПУСК -----------------
root.mainloop()
