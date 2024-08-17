import tkinter as tk
from tkinter import messagebox, simpledialog

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        index = task_list.curselection()[0]
        task_list.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def edit_task():
    try:
        index = task_list.curselection()[0]
        old_task = task_list.get(index)
        new_task = simpledialog.askstring("Edit Task", "Edit your task:", initialvalue=old_task)
        if new_task:
            task_list.delete(index)
            task_list.insert(index, new_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit.")

def clear_all():
    task_list.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x450")

# Create GUI elements
task_entry = tk.Entry(root, width=40)
add_button = tk.Button(root, text="Add Task", width=10, command=add_task)
task_list = tk.Listbox(root, width=40, height=15)
remove_button = tk.Button(root, text="Remove Task", width=10, command=remove_task)
edit_button = tk.Button(root, text="Edit Task", width=10, command=edit_task)
clear_button = tk.Button(root, text="Clear All", width=10, command=clear_all)

# Place GUI elements on the window
task_entry.pack(pady=10)
add_button.pack()
task_list.pack(pady=10)
remove_button.pack()
edit_button.pack(pady=5)
clear_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()