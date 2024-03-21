#пример работы с tkinter
#простой интерфейс

import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

def mark_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        upd_item = task_listbox.get(selected_task)+" - выполнено!"
        task_listbox.delete(selected_task)
        task_listbox.insert(selected_task, upd_item)
        task_listbox.itemconfig(selected_task, bg=color3)

color1 = "DarkOliveGreen3"
color2 = "cornsilk"
color3 = "SpringGreen4"

root = tk.Tk()
root.title("Задачи")
root.configure(background=color1)

text = tk.Label(root, text="Введите задачу", bg=color1)
text.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg=color2)
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=5)

delete_task_button = tk.Button(root, text="Удалить задачу", command=delete_task)
delete_task_button.pack(pady=5)

mark_task_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task)
mark_task_button.pack(pady=5)

task_listbox = tk.Listbox(root, height=10, width=50, bg=color2)
task_listbox.pack(pady=10)
new_text = tk.Label(root, text="Список задач")

root.mainloop()