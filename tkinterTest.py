import tkinter as tk

root = tk.Tk()
root.title("Tkinter Test")
root.geometry("400x200")

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack(padx=100, pady=20)
root.mainloop()