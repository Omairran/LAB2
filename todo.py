import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove Selected", command=self.remove_task)
        self.remove_button.pack()

        self.clear_button = tk.Button(root, text="Clear All", command=self.clear_tasks)
        self.clear_button.pack()

        self.task_list = tk.Listbox(root, width=50, height=15)
        self.task_list.pack(pady=10)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def remove_task(self):
        try:
            selected_index = self.task_list.curselection()[0]
            self.task_list.delete(selected_index)
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")

    def clear_tasks(self):
        self.task_list.delete(0, tk.END)
        self.save_tasks()

    def save_tasks(self):
        with open(TASKS_FILE, "w") as f:
            tasks = self.task_list.get(0, tk.END)
            for task in tasks:
                f.write(task + "\n")

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as f:
                for task in f.readlines():
                    self.task_list.insert(tk.END, task.strip())

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
