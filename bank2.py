import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Уралсиб")
root.geometry("1300x750")
root.configure(bg="#e9e9f2")

PRIMARY = "#4b1e78"
DARK = "#3a145f"
LIGHT_BG = "#e9e9f2"

saved_login = ""
saved_password = ""

# ================= ВЕРХНЯЯ ШАПКА =================

top_bar = tk.Frame(root, bg=PRIMARY, height=70)
top_bar.pack(fill="x")

tk.Label(top_bar,
         text="Уралсиб",
         bg=PRIMARY,
         fg="white",
         font=("Segoe UI", 20, "bold")).pack(side="left", padx=30)

# ================= ОСНОВНОЙ КОНТЕЙНЕР =================

main_container = tk.Frame(root, bg=LIGHT_BG)
main_container.pack(fill="both", expand=True)

# ================= ЛЕВАЯ ПАНЕЛЬ =================

left = tk.Frame(main_container, bg="#5a2d91", width=300)
left.pack(side="left", fill="y")

left.pack_propagate(False)

tk.Entry(left, font=("Segoe UI", 12)).pack(pady=(50, 10), ipadx=10, ipady=8)
password_entry = tk.Entry(left, show="*", font=("Segoe UI", 12))
password_entry.pack(pady=10, ipadx=10, ipady=8)

tk.Checkbutton(left,
               text="Запомнить логин",
               bg="#5a2d91",
               fg="white",
               selectcolor="#5a2d91").pack(pady=10)

def styled_btn(parent, text, cmd):
    return tk.Button(parent,
                     text=text,
                     command=cmd,
                     bg=DARK,
                     fg="white",
                     font=("Segoe UI", 11, "bold"),
                     relief="flat",
                     activebackground="#2a0d47")

styled_btn(left, "АВТОРИЗОВАТЬСЯ", lambda: None).pack(pady=10, ipadx=10, ipady=8)

tk.Label(left,
         text="Это длинный текст перед...",
         bg="#5a2d91",
         fg="white",
         font=("Segoe UI", 9)).pack(pady=10)

styled_btn(left, "ЗАРЕГИСТРИРОВАТЬСЯ", lambda: None).pack(pady=10, ipadx=10, ipady=8)

# ================= ЦЕНТР =================

center = tk.Frame(main_container, bg=LIGHT_BG)
center.pack(side="left", expand=True, fill="both")

tk.Label(center,
         text="УМНАЯ СИСТЕМА ПЕРЕВОДОВ\nС ВНЕДРЕНИЕМ СОВРЕМЕННЫХ ИИ!",
         bg=LIGHT_BG,
         font=("Segoe UI", 16, "bold")).pack(pady=40)

card = tk.Frame(center, bg=PRIMARY, padx=30, pady=30)
card.pack(pady=20)

tk.Label(card,
         text="Уралсиб Business",
         bg=PRIMARY,
         fg="white",
         font=("Segoe UI", 14, "bold")).pack(pady=10)

card_entry = tk.Entry(card, font=("Segoe UI", 12), width=35)
card_entry.pack(pady=10, ipady=6)

row = tk.Frame(card, bg=PRIMARY)
row.pack(pady=5)

date_entry = tk.Entry(row, font=("Segoe UI", 12), width=12)
date_entry.pack(side="left", padx=5, ipady=6)

cvc_entry = tk.Entry(row, font=("Segoe UI", 12), width=12)
cvc_entry.pack(side="left", padx=5, ipady=6)

tk.Label(card,
         text="Сумма перевода",
         bg=PRIMARY,
         fg="white").pack(pady=(15, 0))

amount_entry = tk.Entry(card, font=("Segoe UI", 12), width=35)
amount_entry.pack(pady=5, ipady=6)

tk.Label(card,
         text="Сообщение получателю",
         bg=PRIMARY,
         fg="white").pack(pady=(15, 0))

message_entry = tk.Entry(card, font=("Segoe UI", 12), width=35)
message_entry.pack(pady=5, ipady=6)

styled_btn(card, "ПЕРЕВЕСТИ", lambda: None).pack(pady=20, ipadx=30, ipady=8)

# ================= ПРАВАЯ ПАНЕЛЬ =================

right = tk.Frame(main_container, bg="white", width=300)
right.pack(side="right", fill="y")
right.pack_propagate(False)

tk.Label(right,
         text="НАМ ДОВЕРЯЮТ",
         bg="white",
         font=("Segoe UI", 12, "bold")).pack(pady=20)

try:
    img = Image.open("trusted.png")
    img = img.resize((260, 550))
    photo = ImageTk.PhotoImage(img)
    tk.Label(right, image=photo, bg="white").pack()
except:
    tk.Label(right, text="(Нет картинки)", bg="white").pack()

root.mainloop()
