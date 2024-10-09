import tkinter as tk
from tkinter import messagebox, simpledialog

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def __str__(self):
        return self.title

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []

        # Set up the GUI
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry = tk.Entry(self.root, width=52)
        self.entry.pack(pady=10)

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=10)

        self.complete_task_button = tk.Button(self.root, text="Complete Task", command=self.complete_task)
        self.complete_task_button.pack(pady=10)

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=10)

    def add_task(self):
        task_title = self.entry.get()
        if task_title:
            new_task = Task(task_title)
            self.tasks.append(new_task)
            self.update_task_list()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index].completed = True
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to complete.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_title = f"{task.title} {'(Completed)' if task.completed else ''}"
            self.task_listbox.insert(tk.END, display_title)

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()
