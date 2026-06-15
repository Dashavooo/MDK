import pymysql
import tkinter as tk
from tkinter import messagebox

connection = pymysql.connect(
    host="192.168.200.18",
    user="IS_52",
    password="JrP7eSiQuf",
    database="IS_52",
    ssl_disabled=True,
    charset="utf8mb4"
)

cursor = connection.cursor()
cursor.execute("SET NAMES utf8mb4")

cursor.execute("""
CREATE TABLE IF NOT EXISTS volchkova_mizgiris_game_server (
    server_id INT PRIMARY KEY AUTO_INCREMENT,
    game_name VARCHAR(100),
    server_name VARCHAR(100),
    slots INT,
    price_per_month DECIMAL(10,2),
    ram_gb INT,
    location VARCHAR(100),
    status VARCHAR(50),
    owner_name VARCHAR(100)
)
""")

connection.commit()


def add_server():
    cursor.execute(
        "INSERT INTO volchkova_mizgiris_game_server "
        "(game_name, server_name, slots, price_per_month, ram_gb, location, status, owner_name) "
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        (
            game_name.get(),
            server_name.get(),
            slots.get(),
            price.get(),
            ram.get(),
            location.get(),
            status.get(),
            owner.get()
        )
    )
    connection.commit()
    messagebox.showinfo("Готово", "Сервер добавлен")

def show_servers():
    cursor.execute("SELECT * FROM volchkova_mizgiris_game_server")
    result.delete("1.0", tk.END)

    for row in cursor.fetchall():
        result.insert(tk.END, str(row) + "\n")

def update_server():
    cursor.execute(
        "UPDATE volchkova_mizgiris_game_server SET game_name=%s, server_name=%s, slots=%s, "
        "price_per_month=%s, ram_gb=%s, location=%s, status=%s, owner_name=%s "
        "WHERE server_id=%s",
        (
            game_name.get(),
            server_name.get(),
            slots.get(),
            price.get(),
            ram.get(),
            location.get(),
            status.get(),
            owner.get(),
            server_id.get()
        )
    )
    connection.commit()
    messagebox.showinfo("Готово", "Сервер обновлён")

def delete_server():
    cursor.execute(
        "DELETE FROM volchkova_mizgiris_game_server WHERE server_id=%s",
        (server_id.get(),)
    )
    connection.commit()
    messagebox.showinfo("Готово", "Сервер удалён")

root = tk.Tk()
root.title("Аренда игровых серверов")
root.geometry("950x550")
root.configure(bg="#eaf3ff")

# левая часть
left = tk.Frame(root, bg="#eaf3ff")
left.grid(row=0, column=0, padx=25, pady=20, sticky="nw")

# правая часть
right = tk.Frame(root, bg="#eaf3ff")
right.grid(row=0, column=1, padx=20, pady=20, sticky="nw")

labels = [
    "ID",
    "Название игры",
    "Название сервера",
    "Слоты",
    "Цена за месяц",
    "ОЗУ",
    "Локация",
    "Статус",
    "Владелец"
]

entries = []

for i in range(len(labels)):
    tk.Label(
        left,
        text=labels[i],
        bg="#eaf3ff",
        fg="#1f3b57",
        font=("Arial", 10, "bold")
    ).grid(row=i, column=0, sticky="w", pady=4)

    entry = tk.Entry(left, width=28)
    entry.grid(row=i, column=1, pady=4, padx=10)

    entries.append(entry)

server_id = entries[0]
game_name = entries[1]
server_name = entries[2]
slots = entries[3]
price = entries[4]
ram = entries[5]
location = entries[6]
status = entries[7]
owner = entries[8]

# кнопки слева
tk.Button(left, text="Добавить", command=add_server, bg="#4caf50", fg="white", width=18).grid(row=9, column=0, pady=8)
tk.Button(left, text="Показать", command=show_servers, bg="#2196f3", fg="white", width=18).grid(row=9, column=1, pady=8)
tk.Button(left, text="Редактировать", command=update_server, bg="#ff9800", fg="white", width=18).grid(row=10, column=0, pady=5)
tk.Button(left, text="Удалить", command=delete_server, bg="#f44336", fg="white", width=18).grid(row=10, column=1, pady=5)

# окно вывода справа
tk.Label(
    right,
    text="Вывод данных",
    bg="#eaf3ff",
    fg="#1f3b57",
    font=("Arial", 12, "bold")
).pack(anchor="w")

result = tk.Text(
    right,
    width=65,
    height=25,
    bg="white",
    fg="black"
)
result.pack()
root.mainloop()